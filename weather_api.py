import requests
import json
Key = "a56cdd37810f0a936a6db3bcadd4188c"



def callWeatherAPI(latitude: tuple, longitude: tuple, key: str) -> dict:
  """
  Builds an API request for the OpenWeather API based on the parameters 
  passed to the function. 
  Response is parsed as a dict and returned.
  """
  
  Base_url = "https://api.openweathermap.org/data/3.0/onecall?"
  request_url = f"{Base}lat={lat}&lon={lon}&appid={key}"
  response = requests.get(request_url)
  data = json.dumps(response.text)
  print(data)
  


if __name__ == "__main__":

  callWeatherApi((90,90),(180,-180), Key)


  
