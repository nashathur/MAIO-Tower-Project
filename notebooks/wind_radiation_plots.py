# Plots of incoming shortwave radiation (CNR1) and wind speed (Young propeller, ~3 m):
# a time series and a mean diurnal cycle for each, saved as four PNG files in figures/.
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
FIGURES = Path(__file__).resolve().parents[1] / "figures"

# ---------- Load radiation: CNR1, 30-min, CEST ----------
cnr1 = pd.read_csv(DATA / "cnr1.csv")
# doy is a decimal day of the year (1.0 = 1 Jan 00:00); turn it into a date and time
cnr1["time"] = (pd.Timestamp("2025-12-31") + pd.to_timedelta(cnr1["doy"], unit="D")).dt.round("30min")
# drop the two invalid records (15 Sep 14:30 and 28 Sep 14:00, e.g. -22959 W/m2)
cnr1 = cnr1[cnr1["SWTop_Avg"].between(-20, 1400)]
radiation = cnr1.set_index("time")["SWTop_Avg"]

# ---------- Load wind: Young propeller in FLUX_30min, 30-min, CEST ----------
flux = pd.read_csv(DATA / "FLUX_30min.csv", parse_dates=["Time"])
flux = flux.drop_duplicates("Time")  # 1 Oct 00:30 occurs twice
wind = flux.set_index("Time")["Uy"].dropna()

# ---------- Hour of the day for the diurnal cycle ----------
# Each timestamp is the END of a 30-min average, so 13:00 stands for 12:30-13:00.
# Shift by 15 min to plot each value at the middle of its interval (12:45).
rad_time = radiation.index - pd.Timedelta(minutes=15)
rad_hour = rad_time.hour + rad_time.minute / 60
wind_time = wind.index - pd.Timedelta(minutes=15)
wind_hour = wind_time.hour + wind_time.minute / 60

# ---------- Plot 1: radiation time series ----------
fig, ax = plt.subplots(figsize=(10, 3.5))
ax.plot(radiation.index, radiation, color="tab:orange", lw=0.8)
ax.set_title("Shortwave Radiation Timeseries")
ax.set_xlabel("time")
ax.set_ylabel("SW$_{in}$ [W/m$^2$]")
ax.set_xlim(radiation.index[0], radiation.index[-1])
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
ax.grid(alpha=0.3)
fig.savefig(FIGURES / "radiation_timeseries.png", dpi=200, bbox_inches="tight")

# ---------- Plot 2: radiation mean diurnal cycle ----------
rad_mean = radiation.groupby(rad_hour).mean()
rad_q25 = radiation.groupby(rad_hour).quantile(0.25)
rad_q75 = radiation.groupby(rad_hour).quantile(0.75)

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.fill_between(rad_mean.index, rad_q25, rad_q75, color="tab:orange", alpha=0.25, lw=0, label="25–75 %")
ax.plot(rad_mean.index, rad_mean, color="tab:orange", label="mean")
ax.set_title("Diurnal Cycle of Shortwave Radiation")
ax.set_xlabel("hour (CEST)")
ax.set_ylabel("SW$_{in}$ [W/m$^2$]")
ax.set_xlim(0, 24)
ax.set_xticks(range(0, 25, 6))
ax.grid(alpha=0.3)
ax.legend(fontsize=8, loc="upper left")
fig.savefig(FIGURES / "radiation_diurnal.png", dpi=200, bbox_inches="tight")

# ---------- Plot 3: wind speed time series ----------
fig, ax = plt.subplots(figsize=(10, 3.5))
ax.plot(wind.index, wind, color="tab:blue", lw=0.8)
ax.set_title("Wind Speed Timeseries")
ax.set_xlabel("time")
ax.set_ylabel("wind speed [m/s]")
ax.set_xlim(wind.index[0], wind.index[-1])
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
ax.grid(alpha=0.3)
fig.savefig(FIGURES / "wind_timeseries.png", dpi=200, bbox_inches="tight")

# ---------- Plot 4: wind speed mean diurnal cycle ----------
wind_mean = wind.groupby(wind_hour).mean()
wind_q25 = wind.groupby(wind_hour).quantile(0.25)
wind_q75 = wind.groupby(wind_hour).quantile(0.75)

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.fill_between(wind_mean.index, wind_q25, wind_q75, color="tab:blue", alpha=0.25, lw=0, label="25–75 %")
ax.plot(wind_mean.index, wind_mean, color="tab:blue", label="mean")
ax.set_title("Diurnal Cycle of Wind Speed")
ax.set_xlabel("hour (CEST)")
ax.set_ylabel("wind speed [m/s]")
ax.set_xlim(0, 24)
ax.set_xticks(range(0, 25, 6))
ax.grid(alpha=0.3)
ax.legend(fontsize=8, loc="upper left")
fig.savefig(FIGURES / "wind_diurnal.png", dpi=200, bbox_inches="tight")

plt.show()
