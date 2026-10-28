# Temperature difference from the Vaisala at 4 m (dT = sensor - Vaisala) against incoming
# shortwave radiation (CNR1), daytime only, one panel per sensor. Saved in figures/.
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
FIGURES = Path(__file__).resolve().parents[1] / "figures"
DAYTIME = 20  # W/m2: records with more incoming shortwave than this count as daytime

# ---------- Load profile mast: Vaisala at 4 m (T2), 30-min, CEST ----------
profile = pd.read_csv(DATA / "profile.csv")
# DOY is a decimal day of the year (1.0 = 1 Jan 00:00); turn it into a date and time
profile["time"] = (pd.Timestamp("2025-12-31") + pd.to_timedelta(profile["DOY"], unit="D")).dt.round("30min")
profile = profile.iloc[1:]  # the first record (15 Sep 14:30) is invalid
profile = profile.set_index("time")

# ---------- Load CNR1: incoming shortwave and body temperature, 30-min, CEST ----------
cnr1 = pd.read_csv(DATA / "cnr1.csv")
cnr1["time"] = (pd.Timestamp("2025-12-31") + pd.to_timedelta(cnr1["doy"], unit="D")).dt.round("30min")
cnr1 = cnr1[cnr1["SWTop_Avg"].between(-20, 1400)]  # drops the two invalid records
cnr1 = cnr1.set_index("time")

# ---------- Load iWS: T sensor, RH/T sensor and CNR4 body temperature, 30-min, UTC ----------
iws = pd.read_csv(DATA / "iws.csv")
iws["time"] = pd.to_datetime(dict(year=iws["year"], month=iws["mm"], day=iws["dd"],
                                  hour=iws["hh"], minute=iws["minutes"]))
iws["time"] = iws["time"] + pd.Timedelta(hours=2)  # UTC -> CEST, like the other files
iws = iws.replace(327.67, np.nan)  # 327.67 is the iWS fill value
iws = iws.set_index("time")

# ---------- Load FLUX: sonic Ts and thermocouples Tc1, Tc2, 30-min, CEST, in kelvin ----------
flux = pd.read_csv(DATA / "FLUX_30min.csv", parse_dates=["Time"])
flux = flux.drop_duplicates("Time")  # 1 Oct 00:30 occurs twice
flux = flux.set_index("Time")

# ---------- Put everything in one table on the same timestamps ----------
df = pd.DataFrame({
    "SWin": cnr1["SWTop_Avg"],
    "Vaisala 4m": profile["T2"],
    "temperature sensor": iws["THUTavg"],
    "humidity sensor": iws["RHTavg"],
    "radiation sensor": iws["NRTavg"],
    "CNR1": cnr1["cnr1_T_C_Avg"],
    "Deduced from anemometer": flux["Ts"] - 273.15,
    "Thermocouple anemometer (to 27 Sep)": flux["Tc"] - 273.15,
    "Thermocouple vert. propeller": flux["Tc2"] - 273.15,
})

# CNR1 body temperature is biased until the logger repair on 28 Sep 13:00-13:30
df.loc[df.index < "2026-09-28 14:00", "CNR1"] = np.nan
# Tc1 logs strange values from 28 Sep onwards; spikes more than 3 K from Ts are removed as well
df.loc[df.index >= "2026-09-28", "Thermocouple anemometer (to 27 Sep)"] = np.nan
spikes = (df["Thermocouple anemometer (to 27 Sep)"] - df["Deduced from anemometer"]).abs() > 3
df.loc[spikes, "Thermocouple anemometer (to 27 Sep)"] = np.nan

day = df[df["SWin"] > DAYTIME]

# ---------- Plot: one panel per sensor, same axes everywhere ----------
# sensor colours as in temperature_plots.py, one per sensor
colors = {"temperature sensor": "blue", "humidity sensor": "purple", "radiation sensor": "red",
          "CNR1": "orange", "Deduced from anemometer": "magenta",
          "Thermocouple anemometer (to 27 Sep)": "brown", "Thermocouple vert. propeller": "turquoise"}
bins = np.arange(0, 701, 100)  # 100 W/m2 radiation bins for the mean line

fig, axs = plt.subplots(2, 4, figsize=(15, 7), sharex=True, sharey=True)
for ax, (sensor, color) in zip(axs.flat, colors.items()):
    dT = day[sensor] - day["Vaisala 4m"]
    ax.scatter(day["SWin"], dT, s=4, color=color, alpha=0.3, lw=0)

    # mean dT per radiation bin, plotted at the mean radiation of the bin (bins with < 5 points left out)
    radiation_bin = pd.cut(day["SWin"], bins)
    bin_sw = day["SWin"].groupby(radiation_bin, observed=True).mean()
    bin_dT = dT.groupby(radiation_bin, observed=True).mean()
    bin_n = dT.groupby(radiation_bin, observed=True).count()
    ax.plot(bin_sw[bin_n >= 5], bin_dT[bin_n >= 5], "o-", color="k", label="mean per 100 W/m$^2$")

    ax.axhline(0, color="gray", lw=0.8)
    ax.set_title(sensor)
    ax.grid(alpha=0.3)

axs.flat[-1].axis("off")  # 7 sensors, 8 panels
axs[0, 0].legend(fontsize=8, loc="upper left")
for ax in axs[1]:
    ax.set_xlabel("SW$_{in}$ [W/m$^2$]")
    ax.tick_params(labelbottom=True)
for ax in axs[:, 0]:
    ax.set_ylabel("ΔT [C]")
fig.suptitle("Temperature Difference from Vaisala 4m vs Shortwave Radiation")
fig.tight_layout()
fig.savefig(FIGURES / "dT_radiation.png", dpi=200, bbox_inches="tight")

plt.show()
