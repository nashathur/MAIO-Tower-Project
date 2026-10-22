# MAIO Project 1: Flux mast temperature sensors

Group project for the MAIO course (Utrecht University), Project 1: comparison of sensors on the MAIO measurement tower at Utrecht Science Park (De Uithof).

## Research question

> How do wind speed and solar radiation influence air temperature measurements from ventilated and unventilated sensors at the MAIO measurement tower?

Several sensors on the tower measure temperature at roughly the same height but differ in measurement principle, ventilation and radiation shielding. The project compares their temperatures and relates the differences to wind speed and radiation.

## Sensors

The tower has five measurement levels at logarithmically increasing heights (8, 4, 2, 1 and 0.5 m).

| Sensor | Measurement principle | Approx. height (m) | Ventilation and shielding |
|---|---|---|---|
| Vaisala HMP110 | Direct air temperature | 0.5, 1, 2, 4, 8 | Mechanically ventilated, shielded |
| iWS temperature sensor and RH/T sensor | Direct temperature | 4 | Unventilated, inside the nylon iWS housing |
| Fine-wire thermocouples Tc and Tc2 | Thermoelectric voltage | 4 (Tc), unknown (Tc2) | None |
| Sonic anemometer (CSAT3) | Speed of sound (sonic temperature Ts) | 4 | None |
| CNR1 and CNR4 radiometers | Radiometer body temperature | about 4 | Sun shield |

Wind is measured by the sonic anemometer, a Young propeller vane, a vertical propeller and the profile cup anemometers; radiation by the CNR1 (large MAIO logger) and CNR4 (iWS station) net radiometers.

## Approach

1. Select the relevant variables from the different datasets.
2. Bring all data to the same, coarsest, time resolution and the same timestamp convention (e.g. 15:00–16:00 stored under 15:00) to avoid shifts.
3. Merge all variables into one dataset.
4. Compare the temperature sensors with each other (correlation statistics), starting small and widening step by step.
5. Explain the differences with wind speed and radiation.

## Variables used

| Instrument group | Contents | File (`data/`) | Columns |
|---|---|---|---|
| Profile mast | Vaisala T and RH, wind speed and direction at 8, 4, 2, 1, 0.5 m | `profile.csv` | `rh1`–`rh5`, `T1`–`T5`, `U1`/`dd1`–`U5`/`dd5` |
| iWS weather station | iWS temperature, RH sensor temperature, RH, wind, pressure | `iws.csv` | `THUTavg`, `RHTavg`, `RHWavg`, `HWSavg`, `HWSstd`, `HWDavg`, `BAP` |
| Radiation, CNR4 | SW and LW in/out, body temperature | `iws.csv` | `NRUavg`, `NRLavg`, `NRIUavg`, `NRILavg`, `NRTavg` |
| Radiation, CNR1 | SW and LW in/out (also +3 °C corrected LW), body temperature, albedo, net radiation | `cnr1.csv` | `SWTop_Avg`, `SWBottom_Avg`, `LWTopC_Avg`, `LWBottomC_Avg`, `LWTopC_Avg_biased`, `LWBottomC_Avg_biased`, `cnr1_T_C_Avg`, `albedo_Avg`, `Rn_Avg` |
| Sonic anemometer and thermocouple Tc | Ts, Tc, wind components, covariances for u* and fluxes | `FLUX_30min.csv` | `u`, `v`, `w`, `Ts`, `Tc`, `uw`, `vw`, `wTs`, `wTc`, `TsTs`, `TcTc` |
| Young propellers and thermocouple Tc2 | Horizontal wind speed and direction, vertical propeller, Tc2, variances | `FLUX_30min.csv` | `Uy`, `WDy`, `wg`, `Tc2`, `uyuy`, `wgwg`, `T2T2` |

u* follows from the covariances as u\* = (uw² + vw²)^¼.

## Known data issues

- **iWS thermocouples**: `TC1avg` and `TC2avg` in `iws.csv` jump between about 30 and 330 °C, so they are not usable; 327.67 is a fill value in several iWS columns. Reported to the supervisor.
- **iWS housing**: the nylon housing is slightly translucent, so solar radiation heats the iWS T and RH/T sensors (T sensor > T air, RH chamber < RH air), mostly by day.
- **CNR1 temperature bias**: the CNR1 body temperature was biased until 28-09-2026 13:00–13:30 LT, when an offset resistor in the logger was replaced. `LWTopC_Avg_biased` and `LWBottomC_Avg_biased` use a rough +3 °C correction; comparing with the CNR4 could estimate the real bias.
- **Time zones**: iWS times are UTC; the profile mast, CNR1, turb and FLUX files are CEST. All loggers stamp a 30-min average at the end of its interval. Checked against solar noon (11:29 UTC in Utrecht) and by lagged correlation; `notebooks/temperature_plots.ipynb` shows the shifts used.
- **Flow distortion**: the mast and neighbouring sensors disturb the wind for some directions; check sensor ratios against wind direction.
- **Data periods**: all files cover 15 Sep to 12 Oct 2026. `cnr1raw.csv` and `profile1min.csv` start on 8 Sep, but their values are invalid until 15 Sep 14:01 (see below).

## Problems found in the data

Found while converting and checking the files in `data/`. Times are as stored in each file.

| File | Problem | Suggested handling |
|---|---|---|
| `iws.csv` | The radiometer calibration constants (`NRUcal`, `NRLcal`, `NRIUcal`, `NRILcal`) and `NRID` change at 22 Sep 00:00, from 10.1/20.2/10.1/10.1 to 13.76/14.76/9.85/11.38. At the same moment the median CNR4/CNR1 shortwave-in ratio drops from 1.04 to 0.82. | Do not combine CNR4 radiation from before and after 22 Sep without a correction; ask the supervisor which constants are right. |
| `iws.csv` | Gaps from 16 Sep 13:00 to 14:00 and from 21 Sep 12:00 to 22 Sep 00:00. | Leave as missing. |
| `iws.csv` | `TC1avg`/`TC2avg` range from 29.7 to 327.67 °C (327.67 occurs 232 and 80 times); `xTSTR1`–`xTSTR8` are always 327.67. | Do not use; use `THUTavg` for the iWS temperature. |
| `iws.csv` | The format doc lists 71 columns, the file has 70. The data matches the doc up to `VBAT` (column 54). | Columns after `VBAT` are named in doc order; `xSTATUS` is left out. Do not rely on them. |
| `profile1min.csv`, `cnr1raw.csv` | Values before 15 Sep 14:01 are installation values (e.g. T about −100 °C, negative RH and radiation): 21 and 141 rows. | Drop rows before 15 Sep 14:01. |
| `profile.csv` | Wind speed `U1`–`U5` is missing until 16 Sep 16:30 (52 rows). | Start wind comparisons on 16 Sep 16:30. |
| `cnr1.csv` | Invalid values (e.g. SW in −22959 W m⁻²) at 15 Sep 14:30 (first record) and 28 Sep 14:00 (logger repair). | Drop these two records. |
| `profile.csv` | The first record (15 Sep 14:30) is invalid: temperatures about −25 °C, RH about 17 %. | Drop it. |
| `FLUX_30min.csv` | Timestamp 1 Oct 00:30 occurs twice. | Keep one; check which. |
| `FLUX_30min.csv` | Thermocouple `Tc` is mostly missing from 29 Sep onward (no data on 1, 4–6, 10 and 11 Oct) and has spikes 5 to 63 K above `Ts` on 9 and 12 Oct; usually Tc − Ts is −1.0 to +0.4 K. | Remove Tc values more than 3 K from Ts; compare Tc mainly before 29 Sep. |
| `FLUX_CORR_30min.csv` | The 14 Oct delivery was reprocessed: all values differ from the 12 Oct version (mean v and w are now about zero after coordinate rotation). It starts at 15 Sep 00:00 with 29 empty rows. | Use the 14 Oct version (in `data/`); the old one is in `source/`. |
| `turb.csv` | `uH2O`, `vH2O`, `wH2O`, `std_H2O`, `H2O` are empty (no humidity sensor on the sonic). | Ignore. |

Problems in the documentation:

- `cnr1.txt` is described as "1mins averaged", but its records are 30 minutes apart.
- `profile1min.txt` has no format description; it has the same 25 columns as `profile.txt`.
- The FLUX header doc ends with `wgTc2`; the files have `wgT2` and `T2T2`.
- `turb.txt` uses the same names twice (`ww`, `uw`, `w`, `u` for both the sonic and the propellers); in `turb.csv` the propeller ones have a `_prop` suffix.
- The units in the iWS column list show `?` where a degree sign should be, e.g. `TC1avg (?C)`.
- The thermocouple Tc2 height is not given anywhere.

## Repository layout

```
source/      raw data deliveries as received (txt files, column format docs as .docx and .md)
data/        latest delivery of each data file as CSV with column headers
notebooks/   analysis notebooks (temperature_plots.ipynb: time series of all temperature sensors)
figures/     figures saved by the notebooks
Project_1_Fluxmast_Temperature_sensors_2026.*  project assignment
Measures_IMAU_Mast.jpeg  photo of the measurement mast
```

The column definitions are in `source/Data_Tower_project_1-4_15oct2026/fileformat_headers.md`, background literature in `source/Data_Tower_projects_1-4_8oct2026_/MAIO_background&iterature.md`.

## Using this repository on your own PC

### One-time setup

1. Install Git from <https://git-scm.com/downloads> (on Windows keep the default options). Alternatively, install [GitHub Desktop](https://desktop.github.com/) if you prefer buttons over commands; the steps below map to its *Clone*, *Fetch/Pull*, *Commit* and *Push* buttons.
2. Tell Git who you are (once per PC):

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

3. To push changes you need write access: ask the repository owner to add your GitHub account under *Settings → Collaborators*. Reading and cloning works without it.
4. Clone the repository into a folder of your choice:

   ```bash
   git clone https://github.com/nashathur/MAIO-Tower-Project.git
   cd MAIO-Tower-Project
   ```

   The first push asks you to sign in to GitHub in the browser.

### Daily workflow

Always get the latest version before you start working:

```bash
git pull
```

After changing or adding files, check what changed, then save and upload it:

```bash
git status
git add <file or folder>
git commit -m "Short description of what you changed"
git push
```

If `git push` is rejected because someone else pushed first, run `git pull` and then `git push` again. If `git pull` reports a conflict, open the listed files, keep the right lines between the `<<<<<<<` and `>>>>>>>` markers, remove the markers, then `git add` the files and `git commit`.

### Tips

- Pull before you start and push when you finish, so everyone works on the latest files.
- Work on separate files (e.g. one script or notebook each) to avoid conflicts; notebooks (`.ipynb`) and Word files are hard to merge when two people edit them at once.
- Commit small, related changes with a clear message; it makes the history readable.
- Do not commit large generated files or personal data; add them to `.gitignore` instead.
