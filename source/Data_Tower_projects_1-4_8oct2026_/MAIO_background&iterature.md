**General background: many of the research questions defined in the projects related to the MAIO mast measurements are discussed in the following literature**

Very good introduction and specifically dedicated to University students

https://www1.muk.uni-hannover.de/hp-design2020/pdf/D%20III%20307%20Transport%20in%20the%20Atmosphere-%20Vegetation%20-%20Soil%20Continuum,%20Moene,%20van%20Dam.pdf

**Temperature measurements**

Radiation shield protection of temperature measurements

<https://link.springer.com/article/10.1007/s10546-009-9430-2>

paper on excess temperatures for shielded naturally ventilated T sensors

<https://journals.ametsoc.org/view/journals/atot/22/7/jtech1762_1.xml>

**Background for the iWS station T measurements**

In the picture below the instrument boom on the iWS weather station is shown with from left to right the iWS unit, a propellor vane sensor and the CNR4 net-radiometer.

Below that a cross section of the IWS unit is shown including the temperature sensor and the temperature/humidity sensor. The design shown here is the same as employed at the MAIO mast representing the 1st version of this type of weather station.

As indicated in the text below the 3D printed external casing of the iWS unit consists of nylon which was chosen for its robustness and UV stability. However, it also is not very opaque to light which makes it less ideal especially in polar regions where snow and ice result in high surface albedo.

<img src="MAIO_background&amp;iterature_images/media/image1.png" style="width:6.26806in;height:4.66944in" />

The Tsensor at the left is mounted inside a radiation hut at the bottom of the iWS housing. Due to the use of nylon this is somewhat translucent to light and solar radiation heats the temperature sensor depending on incoming/reflected solar radiation and wind speed. Hence mosty Tsensor \> Tair in particular during daytime. During nighttime longwave radiation differences and wind speed can also cause differences between Tsensor and Tair.

The specific problem for the temperature/humidity sensor is explained below. The tiny Rh/T sensor is mounted at the bottom of the iWS housing consisting of nylon. There is a small opening present to allow air exchange between the outside air and the small chamber in which the Rh/T sensor is present. Since the iWS housing is partly translucent to light, solar radiation efectively heats the Rh/T sensor and chamber air thereby modifying the air inside the chamber: Tchamber \> Tair and RHchamber \< RHair

<img src="MAIO_background&amp;iterature_images/media/image2.png" style="width:6.26806in;height:4.31042in" />

**background on thermocouple measurements and their sensitivity to radiation/wind**

<https://journals.ametsoc.org/view/journals/atot/11/3/15200426_1994_011_0680_tetoar_2_0_co_2.xml>

thermocouple type that is used:

<https://www.campbellsci.com/products/fw3>

**net_radiometers**

Two types of net-radiation sensors are mounted at the same height at the MAIO mast - KIPP CNR1 and CNR4. The CNR1 is monitored by the large datalogger box together with all the profile measurements. The CNR4 is monitored with the iWS small weather station – both are mounted at one horizontal boom about 4m high in a South West direction. The CNR1 is mounted on a comparable horizontal boom also at about 4m high in a South East direction.

Next to 4 individual radiation sensors both net-radiometers also have an internal temperature sensor to represent the body temperature that is a necessity for correcting the raw longwave radiation data.

From the start of the experiment we noticed that the **temperature from the CNR1 was biased** resulting in biased values for longwave radiation data. At 28-09-2026 between 1300-1330 LT we solved the matter by replacing an offset resistor mounted inside the datalogger box. I corrected for this bias in the dataset in a simple way presuming that the offset in Tcnr1 – I added a roughly estimated +3C offset to the Tcnr1 and also used this to calculate new longwave in and out data (included in the CNR1 data set in columns 16 and 17, respectively).

When you are interested in this flaw in the data and want to improve the Tcnr1 data you are most welcome to do so ☺ and we will give you more information about this ! After the replacement of the resistor inside the logger the TCNR1 and the resulting longwave radiation values should be correct again. By comparing the CNR1 and CNR4 data and temperatures one could e.g. determine the bias in the TCNR1 before 28-09-2026.

**Housing Emission Compensation longwave radiation sensors:** Because the pyrgeometers (lonwave radiometers) themselves absorb and emit long-wave radiation based on their own temperature, raw long-wave voltages must be adjusted using the Stefan-Boltzmann law or manufacturer-supplied calibration formulas factoring in housing temperature (\\(T\_{b}\\)) before final fluxes are logged.

**influence of sampling rate on radiation measurements**

In particular during partly cloudy conditions the variation of the incoming solar radiation is large.

https://www.sciencedirect.com/science/article/pii/0038092X94906629?via%3Dihub

CNR4 specifications

<https://www.kippzonen.com/products/cnr4_net_radiometer>

**Wind speed measurements**

<https://www.annualreviews.org/content/journals/10.1146/annurev.fl.13.010181.002151>

horizontal wind speed Young propellor vane

<https://www.youngusa.com/product/wind-monitor/>

vertical wind speed propellor

https://www.youngusa.com/wp-content/uploads/2025/06/27106R-90D.pdf

Sonic anemometer

https://www.campbellsci.cc/csat3

NOTE: when comparing wind speed measurements in particular the effect of flow distortion can be important depending on wind direction. The wind speed is seriously influenced when e.g. the central mast is “in the way” especially for the wind speed measured by the sonic, iWS or fast sampled propeller vane next to the vertical propeller. Plotting the ratio as a function of wind direction resolves these problems e.g.. Also sensors may influence each other of course. etc…. The absolute value is probably not so much influenced but the differences between sensors can be seriously be affected. Think e.g about the derivation of wind speed gradients from profile measurements - these can be serioulsy affected leading to biased momentum fluxes, roughness lengths, and in the end, sensible heat fluxes.

**sonic anemometer sensor and measurement details**

A sonic anemometer has some special characteristics that makes it useful not only for direct measurement of momentum and sensible heat fluxes but also to estimate latent heat fluxes. Using the difference between the temperature measurements from the sonic and the nearby thermocouple can give some nice options, see paper below:

<http://www.climatexchange.nl/projects/alteddy/papers/Schotanus-1983.pdf>

**energy balance measurements**

The measurement of the surface energy balance is a well known problem in micrometeorology. For the majority of field sites this notoriously leads to an imbalance.

The following literature gives you some basic ideas and strategies on the background and how to deal with this problem.

[**https://link.springer.com/article/10.1007/s007040050070**](https://link.springer.com/article/10.1007/s007040050070)

[https://www.sciencedirect.com/science/article/pii/S016819231100339X](https://www.sciencedirect.com/science/article/pii/S016819231100339X?via%3Dihub)

[doi.org/10.1175/1525-7541(2003)4\<160:EOTSEB\>2.0.CO;2](https://journals.ametsoc.org/view/journals/hydr/4/2/1525-7541_2003_4_160_eotseb_2_0_co_2.xml)

**bulk flux methods & the calculation of turbulence flux from profile tower data**

instead of a Dutch version I found for you in Section 3.6.3 of the book (link given below) an analytic solution to calculate bulk-fluxes. Chapter 3 fully covers an introduction into the problem of surface exchange in particular 3.5 and 3.6 are of importance.

https://www1.muk.uni-hannover.de/hp-design2020/pdf/D%20III%20307%20Transport%20in%20the%20Atmosphere-%20Vegetation%20-%20Soil%20Continuum,%20Moene,%20van%20Dam.pdf
