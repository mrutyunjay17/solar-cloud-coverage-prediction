## Weather Data
### Raw Sky Camera Images
- Total 366 days raw sky camera images are available at frequency of 10 mins.
- The folder name represents date in **MMDD** format and image names are **timestamps** when the image was captured.
- Depending on the month of the year and availability of camera, number of images can be flexible. 
- Mostly the images are from sunrise to sunset.
- Test set folder will not mention any date. So we have to make a general model based on a balanced dataset throughout the year.

### Weather Data Features
#### DATE (MM/DD) and MST
Date and time. Time was measured in 1 min frequency
    
#### Global CMP22 (vent/cor) [W/m^2]
    

#### Direct sNIP [W/m^2]
    

#### Azimuth Angle [degrees]
The angle between the horizontal direction (of the sun, for example) and a reference direction (usually north, although some solar scientists measure the solar azimuth angle from due south)
    
    
#### Tower Dry Bulb Temp [deg C]
    
    
#### Tower Wet Bulb Temp [deg C]
    
    
#### Tower Dew Point Temp [deg C]
    
    
#### Tower RH [%]
    
    
#### Total Cloud Cover [%]
The fraction of the sky dome covered by clouds. This fraction is typically expressed either as tenths (1/10, ..., 10/10) or eighths (1/8, ..., 8/8). Some researchers refer to this as cloud amount, to clarify the distinction from cloud type, which is the nature of the cloud cover.
- -1 stands for night time data when cloud cover data is not captured.
- -7999 and other big negative values are rare in occurrence, and might be due to missing data of cloud cover which can be due to various reasons (e.g, malfunctioning camera).
    
#### Peak Wind Speed @ 6ft [m/s]
Wind speed usually measured by Anemometer
    
#### Avg Wind Direction @ 6ft [deg from N]
    
    
#### Station Pressure [mBar]
Atmospheric Pressure. The pressure (force per area) created by the weight of the atmosphere.
- At higher elevations, the atmospheric pressure is lower because there is less air.
    
#### Precipitation (Accumulated) [mm]<sup>[2](#2.-Precipitable-Water)</sup>
Amount of Precipitable Water. The amount of water in a vertical column of atmosphere.
- The unit of measure is typically the depth to which the water would fill the vertical column if it were condensed to a liquid. For example, 6 centimeters of precipitable water (in the absence of clouds) indicates a very moist atmosphere.
- Precipitable water is often used as a synonym for water vapor
- Derived by integrating atmospheric column moisture.
    
#### Snow Depth [cm]
    
    
#### Moisture 
    
    
#### Albedo (CMP11)
This is the measurement of global and reflected solar raditon.
- Solar albedo, or solar reflectance or solar reflectance, is defined as the ratio of the reflected to the global radiation.
    
    
### Reference Links
<h5 style="font-weight: normal">1. <a href="https://www.nrel.gov/grid/solar-resource/solar-glossary.html">Solar Research Glossary</a></h5>
<h5 style="font-weight: normal">2. <a href="https://www.sciencedirect.com/topics/earth-and-planetary-sciences/precipitable-water">Precipitable Water</a></h5>