# Temperature of every sensor (the four-panel figure of MAIO_FluxMast_Temp2.ipynb) and the hourly
# mean difference from the Vaisala at 4 m. Sensor names follow that notebook; every sensor has its
# own colour. Both figures are saved in figures/.
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
FIGURES = Path(__file__).resolve().parents[1] / "figures"
START, END = pd.Timestamp("2026-09-15 15:30"), pd.Timestamp("2026-10-11 15:30")

# one colour per sensor, used in both figures (dashed lines as in the notebook)
STYLE = {
    "2m": dict(c="goldenrod"),
    "4m": dict(c="green", ls="--"),
    "temperature sensor": dict(c="blue"),
    "humidity sensor": dict(c="purple"),
    "radiation sensor": dict(c="red"),
    "CNR1": dict(c="orange"),
    "Deduced from anemometer": dict(c="magenta"),
    "Thermocouple vert. propeller": dict(c="turquoise"),
    "Thermocouple anemometer": dict(c="brown", ls="--"),
}


def doy_time(doy):
    # doy is a decimal day of the year (1.0 = 1 Jan 00:00); timestamps are CEST
    return (pd.Timestamp("2025-12-31") + pd.to_timedelta(doy, unit="D")).dt.round("30min")


# ---------- Load all temperatures on one 30-min time axis (CEST) ----------
profile = pd.read_csv(DATA / "profile.csv")
profile.index = doy_time(profile["DOY"])

iws = pd.read_csv(DATA / "iws.csv")
iws.index = pd.to_datetime(dict(year=iws["year"], month=iws["mm"], day=iws["dd"],
                                hour=iws["hh"], minute=iws["minutes"])) + pd.Timedelta(hours=2)  # UTC -> CEST
iws = iws.replace(327.67, np.nan)  # 327.67 is the iWS fill value

cnr1 = pd.read_csv(DATA / "cnr1.csv")
cnr1.index = doy_time(cnr1["doy"])

turb = pd.read_csv(DATA / "turb.csv")
turb.index = doy_time(turb["DOY"])

# reindexing to the full time axis matches every sensor on time and leaves data gaps as NaN,
# so lines break at the iWS gap of 21-22 Sep instead of being drawn across it
time = pd.date_range(START, END, freq="30min")
df = pd.DataFrame({
    "2m": profile["T3"],
    "4m": profile["T2"],
    "temperature sensor": iws["THUTavg"],
    "radiation sensor": iws["NRTavg"],
    "humidity sensor": iws["RHTavg"],
    "CNR1": cnr1["cnr1_T_C_Avg"],
    "Deduced from anemometer": turb["Ts"],
    "Thermocouple vert. propeller": turb["Tc2"],
    "Thermocouple anemometer": turb["Tc1"],
}).reindex(time)

# CNR1 body temperature is biased until the logger repair on 28 Sep; Tc1 is unreliable after 27 Sep
df.loc[df.index < "2026-09-28 14:00", "CNR1"] = np.nan
df.loc[df.index > "2026-09-27 15:30", "Thermocouple anemometer"] = np.nan

# ---------- Figure 1: temperature of every sensor, one panel per instrument group ----------
panels = [("Vaisala", ["2m", "4m"]),
          ("iWS", ["temperature sensor", "humidity sensor", "radiation sensor"]),
          ("CNR1", ["CNR1"]),
          ("Sonic Anemometer", ["Deduced from anemometer", "Thermocouple vert. propeller",
                                "Thermocouple anemometer"])]

fig, axs = plt.subplots(4, 1, figsize=(20, 20), sharex=True)
for ax, (title, sensors) in zip(axs, panels):
    for s in sensors:
        ax.plot(df.index, df[s], label=s, **STYLE[s])
    ax.legend(loc=(1.01, 0.68), fontsize=16)
    ax.grid()
    ax.set_ylim(5, 30)  # same range in every panel so they compare directly; data span about 7-28 C
    ax.set_ylabel("temperature [C]", fontsize=16)
    ax.set_title(title, fontsize=24)
    ax.tick_params(labelsize=14)
ax.set_xlim(START, END)
ax.set_xticks(pd.date_range(START, END, freq="D"))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m %H:%M"))
ax.tick_params(axis="x", rotation=45)
ax.set_xlabel("time", fontsize=16)
fig.subplots_adjust(right=0.72, hspace=0.15)
fig.savefig(FIGURES / "temperature_timeseries.png", dpi=150, bbox_inches="tight")

# ---------- Figure 2: hourly mean difference from the Vaisala at 4 m ----------
# difference per 30-min value first, then the mean per hour of the day; each timestamp is the
# end of its 30-min average, so shift by 30 min to put 13:00-13:30 under hour 13
sensors = [s for s in STYLE if s not in ("2m", "4m")]
diff = df[sensors].sub(df["4m"], axis=0)
hourly = diff.groupby((diff.index - pd.Timedelta("30min")).hour).mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.axhline(0, c="black", lw=1)
iws_sensors = ("temperature sensor", "humidity sensor", "radiation sensor")  # no iWS panel title here
for s in sensors:
    ax.plot(hourly.index, hourly[s], marker="o", label=f"iWS {s}" if s in iws_sensors else s, **STYLE[s])
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1))
ax.grid(alpha=0.3)
ax.set_xticks(range(0, 24, 2))
ax.set_xlabel("hour of the day (CEST)")
ax.set_ylabel("ΔT [°C]")
ax.set_title("Difference from Vaisala 4m")
fig.savefig(FIGURES / "hourly_mean_difference.png", dpi=150, bbox_inches="tight")

plt.show()
