import pandas as pd
import numpy as np
import os
import math

DEFAULT_PATH_FOLDER_DATASET = "dataset"
DEFAULT_PATH_FOLDER_TRAINING = os.path.join(DEFAULT_PATH_FOLDER_DATASET,"train")
PRED_TIME_INTERVALS_MINS = [10, 20, 30]
EXPERIEMENT_SEED = 42

FINAL_PRED_COLUMNS = ["30_min_horizon", "60_min_horizon", "90_min_horizon", "120_min_horizon"]

CUSTOM_FEATURE_NAMES = {
    'DATE (MM/DD)':'date',
    'MST':'time',  
    'Global CMP22 (vent/cor) [W/m^2]':'pyranometer',
    'Direct sNIP [W/m^2]':'pyroheliometer',  
    'Azimuth Angle [degrees]':'azimuth_angle_deg',
    'Tower Dry Bulb Temp [deg C]':'tower_dry_bulb_temp_deg', 
    'Tower Wet Bulb Temp [deg C]':'tower_wet_bulb_temp_deg',
    'Tower Dew Point Temp [deg C]':'tower_dew_point_deg', 
    'Tower RH [%]':'tower_rh_pct', 
    'Total Cloud Cover [%]':'total_cloud_coverage_pct',
    'Peak Wind Speed @ 6ft [m/s]':'peak_wind_speed_mps', 
    'Avg Wind Direction @ 6ft [deg from N]':'avg_wind_direction_deg',
    'Station Pressure [mBar]':'station_pressure_mbar', 
    'Precipitation (Accumulated) [mm]':'precipitation_mm',
    'Snow Depth [cm]':'snow_depth_cm', 
    'Moisture':'moisture', 
    'Albedo (CMP11)':'albedometer'
}

def __load_dataset(folder_path = DEFAULT_PATH_FOLDER_TRAINING, csv_dataset_name = "train.csv"):
    '''
        Loads the csv dataset from given folder_path and csv_dataset_file
    '''
    weather_df = pd.read_csv(os.path.join(folder_path, csv_dataset_name))
    return weather_df

def __rename_columns(weather_df, column_mappings = CUSTOM_FEATURE_NAMES):    
    weather_df = weather_df.rename(columns=column_mappings)
    return weather_df

def __add_datetime_column(weather_df):
    column_name = 'datetime'
    column_name_cpy = 'datetime_cpy'
    
    if column_name in weather_df.columns: #If Already renamed
        return weather_df
    
    weather_df[column_name] = pd.to_datetime('2020/'+weather_df['date']+ ' ' + weather_df['time'])
    weather_df[column_name_cpy] = pd.to_datetime('2020/'+weather_df['date']+ ' ' + weather_df['time'])
    cloud_coverage = weather_df['total_cloud_coverage_pct']
    
    weather_df = weather_df.drop(['date', 'time', 'total_cloud_coverage_pct'], axis=1)
    weather_df['total_cloud_coverage_pct'] = cloud_coverage
    return weather_df


def __replace_false_cloud_coverage_with_previous(weather_df):
    '''
        Handle Wrongly labelled data
        Replace total_cloud_coverage_pct < -1 with it's previous minute readings.
        Returns:
            Pands Dataframe
    '''
    weather_df['total_cloud_coverage_pct'] = weather_df.total_cloud_coverage_pct.mask(weather_df.total_cloud_coverage_pct < -1) \
                                                .ffill().astype(int)
    return weather_df

def get_processed_dataset(weather_df = pd.DataFrame(), folder_path = DEFAULT_PATH_FOLDER_TRAINING, csv_dataset_name = "train.csv"):
    
    '''
        Returns pre-processed weather datset with 
        - Renamed Columns
        - Assigned datetime as index and datetime_copy column
        - Handled Falsely Recorded Cloud coverages
        
        Arguments:
            weather_df  : The dataframe will get processed for further ETL operations if provided, 
                    or else provide csv dataset path to load
            folder_path : (Optional) if weather_df = None, then this parameter can be used to load the dataset manually
            csv_dataset_name : (Optional) if weather_df = None, then this parameter can be used to load the dataset manually
        Returns:
            Pandas Dataframe with indexed with datetime 
    '''
    
    if(weather_df.empty):
        weather_df = __load_dataset(folder_path, csv_dataset_name)
    
    #Renames according to default column names
    weather_df = __rename_columns(weather_df)
    #Add and index dataset by datetime column
    weather_df = __add_datetime_column(weather_df)
    weather_df.set_index('datetime', inplace=True)
    #Handle wrongly labelled data
    weather_df = __replace_false_cloud_coverage_with_previous(weather_df)
    return weather_df

def __get_month_day_pairing(weather_df):
    '''
        Returns (Month,Day) pairs present in dataset
    '''
    weather_dict_keys = weather_df.groupby([weather_df.index.month, weather_df.index.day ]).groups.keys()
    return list(weather_dict_keys)

def prepare_usable_dataset(dataset, features = None, months = None):
    
    '''
        Returns weather data only with recorded total percent cloud coverages 
        - Drops feature "datetime_cpy" 
        
        Arguments:
            features - (Optional) If provided, will provide dataset with selected features
            months - (Optional) If provided, will query all days from listed months.
    '''
    
    #Removing non recorded cloud coverages
    mask = (dataset.datetime_cpy.dt.month.isin(months) & (dataset['total_cloud_coverage_pct'] > -1)) if months else (dataset['total_cloud_coverage_pct'] > -1)
    #if not months:
    dataset = dataset.loc[mask] #Import full dataset
    #else:
        #dataset =  dataset.loc[dataset.datetime_cpy.dt.month.isin(months) & (dataset['total_cloud_coverage_pct'] > -1)] #Import selected months
    
    if features:
        dataset = pd.concat([dataset[features], dataset[['total_cloud_coverage_pct']]], axis=1)
    
    #Rescaling total_cloud_coverage_pct to percent values
    dataset['total_cloud_coverage_pct'] = dataset['total_cloud_coverage_pct'] / 100
    #dataset['total_cloud_coverage_pct'] = dataset['total_cloud_coverage_pct']
    
    #Drop datetime column if present
    if 'datetime_cpy' in dataset.columns:
        dataset = dataset.drop(['datetime_cpy'], axis=1)

    return dataset

def __prepare_daywise_chunked_dataset(dataset):
    '''
        Returns dictionary with mintue wise recordings per day for initial 8 hours for easy handling.
        TODO: The 8 hours cap should be changed to varying ranges later.
        
        - key : (month,day) dictionary is shuffled randomly with key
        - value : 
    '''
    
    np.random.seed(EXPERIEMENT_SEED)
    # map month_daywise mapped dictionary
    month_day_pairs = __get_month_day_pairing(dataset)

    dataset_chunked = {}
    min_uptime_duration = np.inf;
    max_uptime_duration = -np.inf;

    for month, day in month_day_pairs:
        daily_chunk = dataset.loc[((dataset.index.month == month) & ( dataset.index.day == day)), :].values
        #TODO: Later Segment active minutes such that only 60 mins spaced time frames are present
        total_daily_active_minutes = np.shape(daily_chunk)[0]
        #Using for max 8 hours of data per day to keep other splits simple
        max_daily_minutes = 8 * 60

        #Segmenting for max 8 hours per day
        dataset_chunked[(month,day)] = daily_chunk[:max_daily_minutes,:]

        if(total_daily_active_minutes < min_uptime_duration):
            min_uptime_duration = total_daily_active_minutes

        if(total_daily_active_minutes > max_uptime_duration):
            max_uptime_duration = total_daily_active_minutes

    print("Shape of a sample day record (8 hours * 60, num_features): {}".format(np.shape(dataset_chunked[next(iter(dataset_chunked))])))
    print("Min-Max Active Uptime in Hours: (%d,%d)\n" % ((min_uptime_duration // 60) ,(max_uptime_duration // 60)))

    dataset_chunked_arr = list(dataset_chunked.items()) 
    
    #Shuffled chunks randomly day wise (Mintues information per day is still intact)
    np.random.shuffle(dataset_chunked_arr)  
    dataset_chunked = dict(dataset_chunked_arr)
    
    print("First Random Three days: ")
    for itr, (key, value) in enumerate(dataset_chunked.items()):
        print(key, end="  ")
        if itr == 2:
            break
    return dataset_chunked


def get_train_test_split(dataset, test_ratio=0.09, best_feature_cols = None, months = None):
    ''' 
        
        Returns Training set, Testing set, Training (Month,Day) indexes, Testing (Month,Day) indexes
        
        Make sure to import dataset through \033[1m"utility.get_processed_dataset()"\033[0m method or similar formatting.
        
        - Drops feature "datetime_cpy" 
        - Filters weather data with only recorded total cloud percentages
        
    '''
    
    dataset = prepare_usable_dataset(dataset, best_feature_cols, months)
    print("Original dataset shape: ", dataset.shape)
    print("----------------------------------------------------------------")
    dataset_chuncked = __prepare_daywise_chunked_dataset(dataset)
    print("\n----------------------------------------------------------------")
    dataset = np.array([arr for arr in dataset_chuncked.values()])
    print("Dataset shape after daywise chunks", dataset.shape)
    print("----------------------------------------------------------------")
    #Splitting dataset into train test
    test_size = math.floor(dataset.shape[0] * test_ratio)
    train, test = dataset[:-test_size,:,:] , dataset[-test_size:,:,:]
    print("Data shape with reference format: [num_instances, num_time_steps, num_features]")
    print("Training shape {} , Testing Shape {}".format(train.shape, test.shape))
    
    #Get month,day indexes for train test for debugging
    month_day_wise_indexes = list(dataset_chuncked.keys())
    train_monthdays, test_monthdays = month_day_wise_indexes[:-test_size], month_day_wise_indexes[-test_size:]
    
    return train, test, train_monthdays, test_monthdays