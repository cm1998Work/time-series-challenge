import requests
import json
from database import openDB, writeToDB, closeDB
Key = "a56cdd37810f0a936a6db3bcadd4188c"


def callWeatherAPI(latitude: tuple, longitude: tuple, key: str) -> dict:
  """
  Builds an API request for the OpenWeather API based on the parameters 
  passed to the function. 
  Response is parsed as a dict and returned.
  """
  
  Base_url = "https://api.openweathermap.org/data/3.0/onecall?"
  request_url = f"{Base_url}lat={latitude}&lon={longitude}&appid={key}&units=metric"
  response = requests.get(request_url)
  data = json.dumps(response.text)
  
  return data

def TransformResponseData(data: dict)->dict:
  """
  Tranforms the API response so that it is ready to be 
  written to the database
  """
  current = data.current
  del current['weather'] #Weather attribute is an object (can't be visualised so delete)
  #do more 
  return current
  
  

  
  


if __name__ == "__main__":

  data = callWeatherAPI((90,90),(180,-180), Key)
  data = transformResponseData(data)
  writeToDB(data)


  
