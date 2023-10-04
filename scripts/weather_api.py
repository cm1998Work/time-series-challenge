import requests
import json
import time
from influxdb_client_3 import Point

Key = "a56cdd37810f0a936a6db3bcadd4188c"


def callWeatherAPI(latitude: float, longitude: float, key: str) -> dict:
   
  """
  Builds an API request for the OpenWeather API based on the parameters 
  passed to the function. 
  Response is parsed as a dict and returned.
  """
  
  Base_url = "https://api.openweathermap.org/data/2.5/weather?"
  request_url = f"{Base_url}lat={latitude}&lon={longitude}&appid={key}&units=metric"
  response = requests.get(request_url)
  data = json.loads(response.text)
  
  return data

def transformResponseData(data: dict)->dict:
  """
  Tranforms the API response so that it is ready to be 
  written to the database
  Inflix DB will accept dictionary style mapping with keys:
  measurement, tags, fields and time
  """
  
  #Access weather data - we will use temp and wind
  temp = data['main']
  wind = data['wind']
  time = data['dt']
  
  #Create data structure which can be written to influx DB
  transformed_data = {
    'measurement':"Weather",
    'tags':{'location':'London'},
    'fields':{},
    'time':time
  }
  for key, value in temp.items():
    transformed_data['fields'][key] = value
  for key, value in wind.items():
    transformed_data['fields'][key] = value
  
  
  print(transformed_data)
  return transformed_data

if __name__ == "__main__":

  data = callWeatherAPI(51.5072, -0.118092, Key) #Latitude and longitude for London passed to function
  transformed_data = transformResponseData(data)
  writeToDB(transformed_data)


  
