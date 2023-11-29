from weather_api import openDb, closeDb
import pandas as pd

def getAllData(db)->pd.DataFrame:
  query = """SELECT  *
  FROM "Weather"
  """
  
  data = db.query(
    query = query,
    database = "challenge",
    language = "sql"
  )

df = table.to_pandas().sort_values(by="time")
print(df)
return df
