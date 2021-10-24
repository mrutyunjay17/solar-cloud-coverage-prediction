import pandas as pd
import os

DEFAULT_PATH_FOLDER_DATASET = "dataset"
DEFAULT_PATH_FOLDER_TRAINING = os.path.join(DEFAULT_PATH_FOLDER_DATASET,"train")

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

def load_dataset(folder_path = DEFAULT_PATH_FOLDER_TRAINING, csv_dataset_name = "train.csv"):
    '''
        Loads the csv dataset from given folder_path and csv_dataset_file
    '''
    weather_df = pd.read_csv(os.path.join(folder_path, csv_dataset_name))
    return weather_df

def get_processed_dataset(weather_df = None, folder_path = DEFAULT_PATH_FOLDER_TRAINING, csv_dataset_name = "train.csv"):
    
    '''
        Get pre-processed weather datset according to data analysis.
        Indexes dataframe with datetime
        weather_df : The dataframe will get processed for further ETL operations if provided, 
                    or else provide csv dataset path to load
        folder_path , csv_dataset_name : (Optional) if weather_df = None, then this parameter can be used to load the dataset manually 
    '''
    
    if(weather_df == None):
        weather_df = load_dataset(folder_path, csv_dataset_name)
    
    #Renames according to default column names
    weather_df = rename_columns(weather_df)
    #Add and index dataset by datetime column
    weather_df = add_datetime_column(weather_df)
    weather_df.set_index('datetime', inplace=True)
    #Handle wrongly labelled data
    weather_df = replace_false_cloud_coverage_with_previous(weather_df)
    return weather_df

def rename_columns(weather_df, column_mappings = CUSTOM_FEATURE_NAMES):    
    weather_df = weather_df.rename(columns=column_mappings)
    return weather_df

def add_datetime_column(weather_df):
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


def replace_false_cloud_coverage_with_previous(weather_df):
    '''
        Handle Wrongly labelled data
        Replace total_cloud_coverage_pct < -1 with it's previous minute readings.
    '''
    weather_df['total_cloud_coverage_pct'] = weather_df.total_cloud_coverage_pct.mask(weather_df.total_cloud_coverage_pct < -1) \
                                                .ffill().astype(int)
    return weather_df

