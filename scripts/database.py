from influxdb_client_3 import InfluxDBClient3, Point



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
  db.write(database=database, r=data)

  closeDB(db)
  


def closeDB(db):
  """
  Closes the connection to the database
  """
  db.close()
