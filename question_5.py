from fastapi import FastAPI
import pandas as pd

app = FastAPI()
#API request funcion
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data/{data}")
async def get_CPI_Data(data: str):
    df = readCSV_into_df()
    if data == "gasoline":
        return get_gasoline_data(df)
    elif data == "allItems":
        return get_allItems_data(df)
    elif data == "allItems-lessfood&energy":
        return get_allItems_lessfoodenergy_data(df)

#DataFrame operations
def readCSV_into_df():
    csvFile = "InflationUSA.csv"
    df = pd.read_csv(csvFile,date_format=["Month"],index_col="Month")
    return df

def get_gasoline_data(dataframe):
    gasoline = dataframe["Gasoline"]
    gasoline.dropna(inplace = True)
    return gasoline

def get_allItems_data(dataframe: pd.DataFrame):
    allItems = dataframe["All items"]
    allItems.dropna(inplace = True)
    return allItems

def get_allItems_lessfoodenergy_data(dataframe: pd.DataFrame):
    allItems_lessfoodenergy = dataframe["All items/less food&energy"]
    allItems_lessfoodenergy.dropna(inplace = True)
    return allItems_lessfoodenergy