**Profile.txt - Profile mast data**

**1, 2, 3, 4, 5 refers to the heights with 1 being the highest**

% 1 jaar

% 2 DOY doy+dec. hours

% 3 hhmm

% 4 Ubatt

% 5 Ptemp

% 6 rh1

% 7 rh2

% 8 rh3

% 9 rh4

% 10 rh5

% 11 T1 8m

% 12 T2 4m

% 13 T3 2m

% 14 T4 1m

% 15 T5 0.5m

% 16 U1 8m

% 17 dd1 wind direction

% 18 U2 4m

% 19 dd2

% 20 U3 2m

% 21 dd3

% 22 U4 1m

% 23 dd4

% 24 U5 0.5m

% 25 dd5

**cnr1raw.txt – individual 10 sec samples of the CNR1 sensor**

**% "TIMESTAMP","SWTop","SWBottom","LWTop","LWBottom","cnr1_T_K"**

% 1 jaar

% 2 doy (incl seconds resolution)

% 3 hhmm

% 4 "SWTop"

% 5 "SWBottom"

% 6 "LWTop" raw data, no Tcnr1 bias correction

% 7 "LWBottom" raw data, no Tcnr1 bias correction

% 8 "cnr1_T_K" (Kelvin)

**CNR1.txt – radiation data logged via the large orange logger box**

**NOTE: column 16 and 17 were additionally included**

% CNR1_DATA 1mins averaged C = 9.97 cal coeffs used inside CAMPBELL logger

% 1 jaar

% 2 doy

% 3 hhmm

% 4 "SWTop_Avg" short wave in

% 5 "SWBottom_Avg" short wave out

% 6 "LWTop_Avg" Longwave in raw

% 7 "LWBottom_Avg" longwave out raw

% 8 "cnr1_T_C_Avg"

% 9 "cnr1_T_K_Avg"

% 10 "LWTopC_Avg" Longwave in

% 11 "LWBottomC_Avg" Longwave out

% 12 "Rs_net_Avg"

% 13 "Rl_net_Avg"

% 14"albedo_Avg"

% 15 "Rn_Avg"

% 16 "LWTopC_Avg_biased" longwave in Tcnr1 biased +3C

% 17 "LWBottomC_Avg_biased" longwave out Tcnr1 biased +3C

**iWS.txt column format**

**A lot of data in here but you only need a few columns/variables**

% 1 year

% 2 mm month

% 3 dd day

% 4 hh

% 5 minutes

% 6 doy Day Of Year incl decimal hours/min/sec

% 7 TC1avg (?C) -9.96 thermocouple data

% 8 TC1std (?C) 0.28 thermocouple data standard deviations

% 9 TC2avg (?C) -10.31 thermocouple data

% 10 TC2std (?C) 0.26 thermocouple data standard deviations

% 11 CJavg (?C) -10.36

% 12 xTSTR1 (?C) -10.14

% 13 xTSTR2 (?C) -10.11

% 14 xTSTR3 (?C) -10.11

% 15 xTSTR4 (?C) -10.11

% 16 xTSTR5 (?C) -10.09

% 17 xTSTR6 (?C) -10.25

% 18 xTSTR7 (?C) -7.52

% 19 xTSTR8 (?C) -4.02

% 20 THUTavg (?C) -10.28 raw Tair

% 21 RHWavg (%) 91.24 raw RHair

% 22 RHTavg (?C) -10.44 raw RH sensor temperature data

% 23 HWSavg (m/s) 6.39 wind speed

% 24 HWSstd (m/s) 0.78 wind speed standard deviation

% 25 HWSmax (m/s) 8.47 wind speed max

% 26 HWDavg (?) 81.65 wind direction

% 27 VWSavg (m/s) 0.00

% 28 VWSstd (m/s) 0.00

% 29 NRUavg (W) 2.4 short wave in

% 30 NRUstd (W) 0.2

% 31 NRLavg (W) 3.0 short wave out

% 32 NRIUavg (W) 263.8 long wave in

% 33 NRILavg (W) 273.8 long wave out

% 34 NRTavg (?C) -10.34 temp from radiation sensor

% 35 NRUcal (?V) 13.73

% 36 NRLcal (?V) 13.37

% 37 NRIUcal (?V) 6.91

% 38 NRILcal (?V) 8.55

% 39 NRID (n) 121096

% 40 BAP (hPa) 794.7 air pressure

% 41 SSH (m) 3.083 sensor heights / changing snow height

% 42 xADW (m) 2.332

% 43 xTBRG (mm) 0.0

% 44 MCH (?) 342.20

% 45 TILTX (?) 1.15

% 46 TILTY (?) -1.27

% 47 LON (?) -470.228.291

% 48 LAT (?) 670.003.638

% 49 HMSL (m) 1.848.078

% 50 PACC (m) 2.43

% 51 SATS (n) 11

% 52 spare 1

% 53 spare 2

% 54 VBAT (V) 5.147

% 55 IDENTIFIER card=1, datalogger=2 or ARGOS=3 data (used to be LBUT (days) )

% 56 STATUS (hex) 0

% 57 iwsID

% 58 xID (n) 58 identifier X is for slave unit data

% 59 xTC1avg (?C) 326.45

% 60 xTC2avg (?C) 326.51

% 61 xCJavg (?C) -10.44

% 62 xTHUTavg (?C) 327.67\`

% 63 xRHWavg (%) 100.00

% 64 xRHTavg (?C) 128.86

% 65 xHWSavg (m/s) 0.00

% 66 xHWDavg (?) 0.52

% 67 xVWSavg (m/s) 0.00

% 68 xSSH (m) 2.074

% 69 xSPARE1 (-) 12op

% 70 xVBAT (V) 3.468

% 71 xSTATUS (hex) 02 station visit indicator !!!

Header for the turbulence data (incl in the file as well). Below I added some comments to some variables

| Time                                         |
|----------------------------------------------|
| U sonic anemometer                           |
| V                                            |
| W                                            |
| Ts sonic                                     |
| Tc thermocouple                              |
| Uu covariances                               |
| Uv                                           |
| Uw                                           |
| uTs                                          |
| uTc                                          |
| Vv                                           |
| Vw                                           |
| Ww                                           |
| wTs                                          |
| wTc                                          |
| TsTs                                         |
| TcTc                                         |
| Uy windspeed from Young horizontal propeller |
| Wdy wind direction from young propeller      |
| Wg vertical windspeed from propeller         |
| Tc2 thermocouple next to vertical propeller  |
| Uyuy                                         |
| Uywg                                         |
| Vyvy                                         |
| Vywg                                         |
| Wgwg                                         |
| wgTc2                                        |

Header voor de turb.txt 30mins gemiddelde ruwe turbulentiedata rechtstreeks uit de logger.

Notice that the data within file “turb.txt” is raw datalogger averaged data.

e.g. to obtain u\* use uw and vw as in txtbooks

u\* = (uw.^2 + vw.^2).^0.25;

% covariances from datalogger 10HZ

First all variables sampled at 10Hz by the sonic anemometer are given

% 1 jaar

% 2 DOY daynumber + decimal hours

% 3 hhmm

% 4 uu

% 5 uv

% 6 uw covariance of u and w component sonic anemometer

% 7 uTs

% 8 uTc1

% 9 uH2O not available

% 10 vv

% 11 vw

% 12 vTs

% 13 vTc1

% 14 vH2O. not available

% 15 ww

% 16 wTs

% 17 wTc1

% 18 wH2O ( g/m3) not available

% 19 std Ts

% 20 std Tc1

% 21 std H2O not available

% 22 u average u component

% 23 v

% 24 w

% 25 Ts sonic temperature

% 26 Tc1 thermocouple temperature close to sonic

% 27 H2O (g/m3) not available

Below are all variables from the fast sampled horizontal propeller vane, vertical propeller and a thermocouple Tc2 (also at 10Hz)

% 28 u vect average wind speed from Young proppeller vane

% 29 dd vect average wind direction from Young proppeller vane

% 30 std dd

% 31 ww

% 32 wu

% 33 wTc2

% 34 uw

% 35 uTc2

% 36 TcTc2

% 37 w

% 38 u

% 39 Tc2

% 40 dd
