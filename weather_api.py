import requests
Key = "a56cdd37810f0a936a6db3bcadd4188c"



def callWeatherAPI(latitude: tuple, longitude: tuple, key: str) -> dict:
  """
  Builds an API request for the OpenWeather API based on the parameters 
  passed to the function. 
  Response is parsed as a dict and returned.
  """
  Base = "https://api.openweathermap.org/data/3.0/onecall?"
  request = f"{Base}lat={lat}&lon={lon}&appid={key
  
  
