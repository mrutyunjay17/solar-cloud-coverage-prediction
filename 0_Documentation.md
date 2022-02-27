# Weather Data
## Raw Sky Camera Images
- Total 366 days raw sky camera images are available at frequency of 10 mins.
- The folder name represents date in **MMDD** format and image names are **timestamps** when the image was captured.
- Depending on the month of the year and availability of camera, number of images can be flexible. 
- Mostly the images are from sunrise to sunset.
- Test set folder will not mention any date. So we have to make a general model based on a balanced dataset throughout the year.
  
  
## Solar Irradiance 
The amount of solar energy that arrives at a specific area of a surface during a specific time interval (radiant flux density).
- A typical unit is W/m^2 .
- It includes visible light as well as non visible parts of spectrum.
- It can reach us by directly, filtered by the clouds, scattered by the atmosphere, reflected by the ground surface.
  
  
## Sunshine Hours
It is the sum of the time intervals (in hours) during which the direct normal solar irradiance exceeds a threshold of 120 W/m².
  
  
## Weather Data Features
### DATE (MM/DD) and MST
Date and time. Time was measured in 1 min frequency.
- We don't have year information for Date and time provided.
    
### Global CMP22 (vent/cor) [W/m^2]
Pyranometer measurements.  
**Pyranometer** - An instrument with a hemispherical field of view, used for measuring total or global solar radiation, specifically global horizontal radiation; a pyranometer with a shadow band or shading disk blocking the direct beam measures the diffuse sky radiation.
- It has 180 degrees field of view angle.
- Solar energy flux varies with the cosine of angle of incidace of radiation. 
- With due and frost deposited on these instruments, we get unreliable data. So they are usually heated.
- Pyraheliometers in combination with Pyranometers are used to monitor the performance of photovoltaic (PV) power plants, by comparing actual output the PV power plant to the expected output based on solar radiation data to calcualte efficiency of the PV power plants.
  
### Direct sNIP [W/m^2]
Measurements by Pyroheliometer.  
**Normal Incidence Pyroheliometer** - It measures solar irradiance coming directly from the sun.
- Pyrheliometers measure direct solar radiation or called *Direct Normal Irradiance*.
- Due to large zero offsets and directional errors in pyranometers, pyroheliometer measuresments are supposed to be more accurate than pyranometers.
- Pyraheliometers in combination with Pyranometers are used to monitor the performance of photovoltaic (PV) power plants, by comparing actual output the PV power plant to the expected output based on solar radiation data to calcualte efficiency of the PV power plants.


  
### Azimuth Angle [degrees]
The angle between the horizontal direction (of the sun, for example) and a reference direction (usually north, although some solar scientists measure the solar azimuth angle from due south)
  
  
  
### Tower Dry Bulb Temp [deg C]
Air temperature measured with a thermometer, similar to ambient temperature. 
- The term "dry-bulb" distinguishes it from the wet-bulb temperature measured by a psychrometer to determine relative humidity.
- Wet-bulb temperature and Dry-bulb temperature are used to compute relative humidity.  
  
  
### Tower Wet Bulb Temp [deg C]
It is the temperature to which air will cool when water is evaporated into unsaturated air measured by a wet-bulb thermometer, which has a wet cloth sleeve that covers its bulb.
- Wet-bulb temperature and Dry-bulb temperature are used to compute relative humidity.  

  
### Tower Dew Point Temp [deg C]
The temperature at which the water in the atmosphere will condense as drops on a surface.
    
  
### Tower RH [%]
Tower Relative Humidity.
- Humidity readily affects the efficiency of the solar cells and creates a minimal layer of water on its surface. It also decreases the efficiency by 10-20% of the total power output produced
  
  
### Total Cloud Cover [%]
The fraction of the sky dome covered by clouds. This fraction is typically expressed either as tenths (1/10, ..., 10/10) or eighths (1/8, ..., 8/8). Some researchers refer to this as cloud amount, to clarify the distinction from cloud type, which is the nature of the cloud cover.
- -1 stands for night time data when cloud cover data is not captured.
- -7999 and other big negative values are rare in occurrence, and might be due to missing data of cloud cover which can be due to various reasons (e.g, malfunctioning camera).
  
  
### Peak Wind Speed @ 6ft [m/s]
Wind speed usually measured by Anemometer
  
  
### Avg Wind Direction @ 6ft [deg from N]
The average wind direction is the arctan of the east/west components divided by the north south components measured in degrees or radians.   
  
  
### Station Pressure [mBar]
Atmospheric Pressure. The pressure (force per area) created by the weight of the atmosphere.
- At higher elevations, the atmospheric pressure is lower because there is less air.
  
  
### Precipitation (Accumulated) [mm]<sup>[2](#2-Precipitable-Water)</sup>
Amount of Precipitable Water. The amount of water in a vertical column of atmosphere.
- The unit of measure is typically the depth to which the water would fill the vertical column if it were condensed to a liquid. For example, 6 centimeters of precipitable water (in the absence of clouds) indicates a very moist atmosphere.
- Precipitable water is often used as a synonym for water vapor
- Derived by integrating atmospheric column moisture.
  
  
### Snow Depth [cm]<sup>[3](#3-Snow-And-Ice-Photovoltaic-Devices)</sup>
If the surface of a PV module is not cleaned and free to capture solar irradiation, the system's perfromance can be highly compromised.
  
  
### Moisture<sup>[2](#2-Precipitable-Water)</sup>
Moisture is the presence of a liquid, especially water, often in trace amounts. 
  
  
### Albedo (CMP11)
Albedometer Measurements.  
**Albedometer** - Measurement of global and reflected solar radiation.
- Solar albedo, or solar reflectance or solar reflectance, is defined as the ratio of the reflected to the global radiation.
    
    
## Reference Links
<h5 style="font-weight: normal">1. <a href="https://www.nrel.gov/grid/solar-resource/solar-glossary.html">Solar Research Glossary</a></h5>
<h5 style="font-weight: normal">2. <a href="https://www.sciencedirect.com/topics/earth-and-planetary-sciences/precipitable-water">Precipitable Water</a></h5>
<h5 style="font-weight: normal">3. <a href="https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2416078/15971_FULLTEXT.pdf?sequence=1">Snow and Ice Photovoltaic Devices</a></h5>
<h5 style="font-weight: normal">4. <a href="http://karpathy.github.io/2015/05/21/rnn-effectiveness/">The Unreasonable Effectiveness of Recurrent Neural Networks by Andrej Karpathy</a></h5>

