import requests
import json
import time
from influxdb_client_3 import InfluxDBClient3, Point


Key = "a56cdd37810f0a936a6db3bcadd4188c"


def callWeatherAPI(latitude: float, longitude: float, key: str) -> dict:

    Base_url = "https://api.openweathermap.org/data/2.5/weather?"
    request_url = f"{Base_url}lat={latitude}&lon={longitude}&appid={key}&units=metric"
    response = requests.get(request_url)
    data = json.loads(response.text)

    return data

def transformResponseData(data: dict)->dict:

    #Access weather data - we will use temp and wind
    temp = data['main']
    wind = data['wind']
    time = data['dt']


    #Create data structure which can be written to influx DB
    transformed_data = {
        'measurement':"Weather",
        'tags':{'location':'London'},
        'fields':{},
    }
    for key, value in temp.items():
        transformed_data['fields'][key] = value
    for key, value in wind.items():
        transformed_data['fields'][key] = value


    print(transformed_data)
    return transformed_data





def openDB():
  """
  Opens a connection to the database and returns
  the database object
  """
  
  host = "https://us-east-1-1.aws.cloud2.influxdata.com"
  token = "Toh-HGqnerXAdabwVlJFWlLUA1nlGlZVQypF8SB9HA6hVeBJTleaAAHz8ymTvXT7JRioe7e5g1FErjVRGHTWfA=="
  org = "Data"
  

  client = InfluxDBClient3(
    host=host,
    token=token,
    org=org
  )
  
  return client
  
  
  return db


def writeToDB(data: dict):
  """
  Writes the data to the database
  """
  db = openDB()
  print(db)
  database = "challenge"

  #write_api = db.write_api(write_options=SYNCHRONOUS)
  db.write(database=database, record=data)

  closeDB(db)
  


def closeDB(db):
  """
  Closes the connection to the database
  """
  db.close()


if __name__ == "__main__":

    data = callWeatherAPI(51.5072, -0.118092, Key) #Latitude and longitude for London passed to function
    transformed_data = transformResponseData(data)
    writeToDB(transformed_data)
