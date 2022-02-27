# Cloud Coverage Prediction

## Project Status
- [x] Data Preprocessing (Tabular)
- [ ] Time Series Modelling (Tabular)
- [ ] Model Evaluation
- [ ] Data Preprocessing (Image + Tabular if needed)
- [ ] Time Series Modelling (Image + Tabular)
- [ ] Model Evaluation

[Download Dataset](https://he-public-data.s3.ap-southeast-1.amazonaws.com/shell_dataset.zip)  

Solar power is one of the fastest-growing renewable energy sources. Global solar photovoltaic (PV) generation is now almost 3% of the total electricity mix and will increase by 15% annually, from 720 TWh in 2019 to almost 3,300 TWh in 2030.  

However, the major challenge with solar PV power production is its intermittency caused by variable weather conditions. Cloud coverage can cast shade over the solar farms in a few minutes and significantly reduce power production. Other factors such as ambient temperature, humidity, and wind speed can also affect the PV temperature and power output. Since grid operations management is based on a delicate balance between supply and demand, any uncertainty in energy production (or consumption) could pose a risk to a grid network.  

Predicting the intermittency in advance can be of tremendous value, in the following ways:  
- Grid operators can schedule deferrable loads to run on clean solar power, increasing the overall share of clean power in the energy mix.
- Producers don't have to sell energy at a low or negative price, having sufficient incentive to run a solar business.  

Cloud coverage remains one of the big risk factors. For example, opaque clouds over the solar farm could reduce the power output by 50-80% in a short interval., causing severe network failures. One way of mitigating this risk requires an accurate prediction of solar irradiance by modeling cloud behavior. Therefore, in this hackathon, we are asking you to predict solar irradiance for short timescales of up to 120 minutes using data-driven models to improve the robustness of the grid.  

### Problem Statement  

#### Predict the percentage of total cloud coverage for the next upcoming intervals using the available weather and sky camera data recorded for 6 hours window..

![image](https://user-images.githubusercontent.com/32392924/137149765-f429108e-aaf5-4820-bdc3-9b7499b32c7a.png)

- Predicting `total_cloud_coverage_pct` in a short time span of 120 minutes *(where average probability of forecast with <30% error varies between 40% to 60% - [Source](https://arxiv.org/abs/1011.3863))* is very challenging for machine learning.
- On this time scale, changes in local cloud cover are driven by a combination of dynamical and physical parameters such as wind speed, wind direction sea-level pressure, humidity, and temperature over the asset of our interest.
- Short interval cloud cover prediction requires accurate estimates of cloud motion and presence using weather data and sky camera images or physics-based weather models or a combination of both.  

We are expected to predict the total cloud coverage as a percentage of the open sky for a fixed field of view at 4 horizon intervals of 30, 60, 90, and 120 minutes from a 6-hour window of historical data.  

While validating and testing the predictions made by model, we are not supposed to consider **DATE (DD)** and **Time MST** in a day as input features.  
So the task at hand is to make a model which will be generic throughout the year. 

### Predict
- Percentage of total cloud cover estimated in the next 30 minutes
- Percentage of total cloud cover estimated in the next 60 minutes
- Percentage of total cloud cover estimated in the next 90 minutes
- Percentage of total cloud cover estimated in the next 120 minutes 

### My Collected Feature Information and References:
- View [**Documentation**](https://github.com/mrutyunjay17/solar-power-prediction/blob/main/Documentation.md) for more information and references.
- Thank you **Amol Sonawane**(Solar Proffessional)[![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/amol-sonawane-971a07144/) for helping as SME for this project.