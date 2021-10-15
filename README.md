# Shell AI Hackathon

[View Challange Specifications](https://www.hackerearth.com/challenges/competitive/shell-ai-hackathon-2021/)  

[Download Dataset](https://he-public-data.s3.ap-southeast-1.amazonaws.com/shell_dataset.zip)  

Solar power is one of the fastest-growing renewable energy sources. Global solar photovoltaic (PV) generation is now almost 3% of the total electricity mix and will increase by 15% annually, from 720 TWh in 2019 to almost 3,300 TWh in 2030.  

However, the major challenge with solar PV power production is its intermittency caused by variable weather conditions. Cloud coverage can cast shade over the solar farms in a few minutes and significantly reduce power production. Other factors such as ambient temperature, humidity, and wind speed can also affect the PV temperature and power output. Since grid operations management is based on a delicate balance between supply and demand, any uncertainty in energy production (or consumption) could pose a risk to a grid network.  

Predicting the intermittency in advance can be of tremendous value, in the following ways:  
- Grid operators can schedule deferrable loads to run on clean solar power, increasing the overall share of clean power in the energy mix.
- Producers don't have to sell energy at a low or negative price, having sufficient incentive to run a solar business.  

Cloud coverage remains one of the big risk factors. For example, opaque clouds over the solar farm could reduce the power output by 50-80% in a short interval., causing severe network failures. One way of mitigating this risk requires an accurate prediction of solar irradiance by modeling cloud behavior. Therefore, in this hackathon, we are asking you to predict solar irradiance for short timescales of up to 120 minutes using data-driven models to improve the robustness of the grid.  

### Problem Statement<sup><a href="https://www.hackerearth.com/challenges/competitive/shell-ai-hackathon-2021/machine-learning/ai-solar-power-prediction-2/">source</a></sup>
The main challenge is to forecast solar irradiance for a specific region of interest given local weather conditions and sky camera images. The problem is divided into 2 levels.&nbsp; As irradiance has a high correlation with cloud coverage the first level of the hackathon is to forecast cloud coverage. In the second level, you will be asked to tackle the complex challenge of predicting solar irradiance to improve the quality of short-term power forecasts.  

#### Level 1:  Predict cloud coverage  
#### Predict the percentage of total cloud coverage for the next upcoming intervals using the available weather and sky camera data.

![image](https://user-images.githubusercontent.com/32392924/137149765-f429108e-aaf5-4820-bdc3-9b7499b32c7a.png)

Predicting cloud cover in a short time span of 120 minutes is very challenging. On this time scale, changes in local cloud cover are driven by a combination of dynamical and physical parameters such as wind speed, wind direction sea-level pressure, humidity, and temperature over the asset of our interest.  

Short interval cloud cover prediction requires accurate estimates of cloud motion and presence using weather data and sky camera images or physics-based&nbsp;weather models or a combination of both.  

We are expected to predict the total cloud coverage as a percentage of the open sky for a fixed field of view at 4 horizon intervals of 30, 60, 90, and 120 minutes from a 6-hour window of historical data.

### Evaluation
The metric to evaluate the perfromance of solution will be MAD (Mean Absolute Deviation)
> ```python
> score = max(0, 100- MAD(actual, predicted))
> ```  

### Submission
- Percentage of total cloud cover estimated in the next 30 minutes
- Percentage of total cloud cover estimated in the next 60 minutes
- Percentage of total cloud cover estimated in the next 90 minutes
- Percentage of total cloud cover estimated in the next 120 minutes

##### Submission Notes:
- The evaluation criteria is based on the Mean Absolute Deviation of your predictions from the actual outcome.
- You will have to upload your output on the problem page in a .csv file.
- The output format will have five columns – scenario_set, 30_min_horizon, 60_min_horizon, 90_min_horizon and 120_min_horizon.  
- The first row of the csv file should be column names followed by 300 rows of predictions for percentage of total cloud cover for 300 scenario sets provided.  - You will not have to submit your code files. A sample submission csv file has been provided for guidance.  

#### References
View [**Documentation.md**](https://github.com/mrutyunjay17/solar-power-prediction/blob/main/Documentation.md) for more information and references.