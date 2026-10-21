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

- **iWS thermocouples**: `TC1avg` and `TC2avg` in `iws.csv` jump between about 50 and 330 °C, so they are not usable; 327.67 is a fill value in several iWS columns. Reported to the supervisor.
- **iWS housing**: the nylon housing is slightly translucent, so solar radiation heats the iWS T and RH/T sensors (T sensor > T air, RH chamber < RH air), mostly by day.
- **CNR1 temperature bias**: the CNR1 body temperature was biased until 28-09-2026 13:00–13:30 LT, when an offset resistor in the logger was replaced. `LWTopC_Avg_biased` and `LWBottomC_Avg_biased` use a rough +3 °C correction; comparing with the CNR4 could estimate the real bias.
- **Time zones**: iWS times are UTC and are shifted to CEST to match the other loggers.
- **Flow distortion**: the mast and neighbouring sensors disturb the wind for some directions; check sensor ratios against wind direction.
- **Data periods**: profile, iWS and CNR1 run from 15 Sep to 12 Oct 2026 (with raw CNR1 and 1-min profile data from 8 Sep); the flux files from 15 Sep to 12 Oct 2026.

## Repository layout

```
source/      raw data deliveries as received (txt files, column format docs as .docx and .md)
data/        latest delivery of each data file as CSV with column headers
Project_1_Fluxmast_Temperature_sensors_2026.*  project assignment
Measures_IMAU_Mast.jpeg  photo of the measurement mast
```

The column definitions are in `source/Data_Tower_project_1-4_15oct2026/fileformat_headers.md`, background literature in `source/Data_Tower_projects_1-4_8oct2026_/MAIO_background&iterature.md`.
