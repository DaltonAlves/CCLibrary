# -*- coding: utf-8 -*-
import pandas as pd

import requests

import json

!wget https://raw.githubusercontent.com/DaltonAlves/CCLibrary/main/cc_lib.csv

#Read CC library csv
df = pd.read_csv("cc_lib.csv")

#API Call and get latitude & longitude values
for i, row in df.iterrows():
  apiAddress = str(df.at[i,'City'])+','+str(df.at[i,'State'])+','+str(df.at[i,'Country'])
  
  parameters = {
      "key" : "", #Use your personal Mapquest API key here!
      "location" : apiAddress
  }

  response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)
  data = json.loads(response.text)['results']

  lat = data[0]['locations'][0]['latLng']['lat']
  lng = data[0]['locations'][0]['latLng']['lng']
  
  df.at[i,"lat"] = lat
  df.at[i,"lng"] = lng

#Save CSV with lat/lng
df.to_csv('cc_lib_GEO.csv')

