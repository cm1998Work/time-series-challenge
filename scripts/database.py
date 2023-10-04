import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS



def openDB():
  """
  Opens a connection to the database and returns
  the database object
  """
  
  url = "https://us-east-1-1.aws.cloud2.influxdata.com"
  token = "Toh-HGqnerXAdabwVlJFWlLUA1nlGlZVQypF8SB9HA6hVeBJTleaAAHz8ymTvXT7JRioe7e5g1FErjVRGHTWfA=="
  org = "f5ccff96eda36a47"
  

  client = influxdb_client.InfluxDBClient(
    url=url,
    token=API_KEY,
    org=org
  )
  
  return client
  
  
  return db


def writeToDB(data: dict):
  """
  Writes the data to the database
  """
  db = openDB()
  bucket = "2a4772c950afd037"

  write_api = db.write_api(write_options=SYNCHRONOUS)
  write_api.write(bucket=bucket, r=data)
  


def closeDB(db):
  """
  Closes the connection to the database
  """
  db.close()



