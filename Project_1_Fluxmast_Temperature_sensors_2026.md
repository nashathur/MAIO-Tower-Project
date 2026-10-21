**Toulouselaan measurement tower**

**Contact: Peter Kuipers Munneke (VMA 3.14), Paul Smeets (VMA 3.56)**

**For the data, contact: Peter Kuipers Munneke after the project start date (p.kuipersmunneke@uu.nl)**

1.  **Comparison of sensors** Multiple instruments at the MAIO mast measure the same variables but have a very different design and are mounted approximately at the same height. The variables for which comparison can be made are temperature, wind speed and radiation. E.g. some temperature sensors are installed at approx. the same height at the MAIO mast, some are ventilated while others are not. Some are shielded, others not. And some are very fast or slow. Also the measurement techniques are different. Many different comparisons can be made and choice for a variable to study has to be made.

Main question: How do the measurements differ, and can you identify a reference sensor and correct measurements from other sensors based on e.g. a fixed offset, or wind and radiation conditions ? How do different measurement techniques influence the results ?

Temperature sensors included are:

- a mechanically ventilated Vaisala HMP110 temp/hum sensor inside the same shielding

- a temperature sensor inside a custom-built iWS housing, unventilated

- a thin wire thermocouple

- a sonic anemometer for which also temperature is available derived via the speed of sound

- temperature sensors inside the CNR1 and CNR4 net-radiometers

Wind speed sensors included are:

- sonic anemometer

- Young propellor vane anemometer

- A vertical propellor anemometer

Radiation measurements:

- CNR1 net-radiometer (logged by the large MAIO datalogger)

- CNR4 net-radiometer (logged by the small iWS weather station)

Background data on meteorological conditions are available: a KIPP CNR1 and CNR4 net-radiometer measuring all individual radiation components, a Young 05103 wind monitor (or wind speed from the sonic anemometer).

Background info:

<http://www.climatexchange.nl/projects/alteddy/papers/Schotanus-1983.pdf>

schotanus1983 sonic anemometer temperature physics (see also section 4 in vanAsselt1991 <https://dare.uva.nl/search?identifier=8bca63be-8bcc-408a-b4e0-bcf33d568170> )

<https://journals.ametsoc.org/view/journals/atot/22/7/jtech1762_1.xml>

paper on excess temperatures for shielded naturally ventilated T sensors

<https://www.wmocimo.net/wp-content/uploads/P1_26_Sotelino_teco_2018_lgs.pdf>

study concerning radiation shelters

**Description of sensors used in weather stations (slow) or at turbulence masts (fast)**

**Fast sensors on the turbulence mast**

<u>Sonic anemometer</u>

The instrument is designed to measure wind velocity components

by transmitting and receiving sonic signals along fixed non-orthogonal directions. Pairs of

transducers act alternately as transmitters and receivers, sending pulses of high frequency

ultrasound between themselves. The times of flight in each direction are measured from

which also a temperature is derived according to Ts = C2/403 with Ts the sonic temperature,

C the speed of sound and 403 a constant (Schotanus et al, 1983). Note that Ts is almost

equal to the virtual temperature. The microcomputer electronics inside the sonic control

box then processes this information and calculates the wind speed in three axes (i.e. u, v,

w). Since there are no moving parts to come into dynamic equilibrium with the air flow, the

Sonic Anemometer/Thermometer responds rapidly to wind velocity fluctuations (the CSAT3

can even be operated in a 60 Hz sampling mode, we us 10Hz to sample the data). It responds linearly to wind velocity and is free from contamination from other velocity components as well as pressure, temperature, and relative humidity. Any calibration of the sensor in the field is not necessary and can be used as an absolute instrument.

<http://www.climatexchange.nl/projects/alteddy/papers/Schotanus-1983.pdf>

<u>Thermocouple (two included, mounted either close to the sonic anemometer or the vertical propellor sensors)</u>

The fine wire thermocouple comprises of a chromel and constantan wire joined at a measurement junction by welding. A voltage potential is

generated when the measurement end of the thermocouple is

at a different temperature than the reference end of the thermocouple (inside the datalogger).

The magnitude of the voltage potential is related to the temperature difference. Therefore,

temperature can be determined by measuring the differences in potential created at the

junction of the two wires and a reference temperature measurement at the reference end of

the thermocouple (inside the datalogger using a different slow sensor). At the MAIO mast we have a thermocouple with a diameter of 0.0762mm.

Important for this type of sensor is the dynamic frequency response of sensors: this describes how well a sensor can monitor the high frequency fluctuations. As an example we could choose the thermocouple, a thin (\<0.1mm) wire thermometer. Due to its size a fine wire can react relatively fast to temperature fluctuations, i.e. the thinner the wire the faster it gets. Nevertheless, the instrument will be limited in response related to its physical dimensions: the more mass the larger the portion of lost high-frequency signal

Characteristics of thermocouples are well described/studied in:

WATER RESOURCES RESEARCH, VOL. 45, W08431, doi:10.1029/2008WR007600, 2009

**Slow sensors at the MAIO mast**

Air temperature Vaisala HMP110 -40 to + 80 <sup>o</sup>C, accuracy 0.3<sup>o</sup>C

Relative humidity Vaisala HMP110 0 to 100%, accuracy 2% (RH\<90% accuracy 1.5%)

Air pressure Vaisala PTB101B 600 to 1060 hPa, accuracy 4 hPa

Wind speed Young 05103 0 to 100 m/s, accuracy 0.1 m/s, threshold 1 m/s

Wind direction Young 05103 0 to 360 degrees, accuracy 2 degrees, threshold 1.1 m/s

Pyranometer Kipp en Zonen CNR1 305 to 2800 nm, accuracy 2%

Pyrradiometer Kipp en Zonen CNR1 5000 to 50000 nm, accuracy 15 Wm−2

Radiation shelter with artificial ventilation (unknown manufacturer)

**Special category - slow sensors sampled fast**

- Vertical and horizontal propellor anemometers
