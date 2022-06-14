import pandas as pd
import numpy as np
import plotly.express as px
import os

#list with the files to be read
l = os.listdir(os.getcwd() + '/dataset/demand')
l.sort()

#adding the path to the list's items
for i in range(len(l)):
    l[i] = os.getcwd() + '/dataset/demand/' + l[i]

#Load to a single column dataframe the timestamps for ease of access.
timeFrame = pd.read_csv(l[0])['Time']
#Create a Dataframe to store all the NaN values for the case of empty csvs of the folder in order to show the abcense of the values in the end graphs.
emptyDF = pd.DataFrame(np.nan, index= range(0, 289), columns=['Day ahead forecast', 'Hour ahead forecast', 'Current demand'])
emptyDF.insert(0, 'Time', timeFrame)

df_demand_list = []
median_dict ={}
for file in l:
    try:    
        temp_dataframe = pd.read_csv(file)
        df_demand_list.append(temp_dataframe)
        median_dict[str(file)[-6:-4]+'/'+str(file)[-8:-6]+'/'+str(file)[-12:-8]] = [temp_dataframe['Day ahead forecast'].median(), temp_dataframe['Hour ahead forecast'].median(), temp_dataframe['Current demand'].median()]
        
    except:
        df_demand_list.append(emptyDF)
        median_dict[str(file)[-6:-4]+'/'+str(file)[-8:-6]+'/'+str(file)[-12:-8]] = [np.nan, np.nan, np.nan]

dayAheadForecast_list = list(median_dict.values())
hourAheadForecastList = []
currentDemandList = []
for i in range(0, len(dayAheadForecast_list)):
    hourAheadForecastList[i] = dayAheadForecast_list[i][1]
    currentDemandList[i] = dayAheadForecast_list[i][2]
    dayAheadForecast_list[i] = dayAheadForecast_list[i][0]




fig = px.line(x = median_dict.keys(), y = dayAheadForecast_list)
fig.show()