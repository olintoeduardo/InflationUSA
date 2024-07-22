import pandas as pd
import plotly.express as px

allitems_foodenergy_csv = "allitems_foodenergy.csv"

#Using the parameters to consider the dataset as time series
allitems_foodenergy_df = pd.read_csv(allitems_foodenergy_csv, parse_dates=["Label"],index_col = "Label")

#Extracting from only 2019 onwards (consider 2018 to calculate annual % change to 2019)
allitems_foodenergy_df = allitems_foodenergy_df[allitems_foodenergy_df.Year >= 2018]

new_df = allitems_foodenergy_df.resample('A').last()
new_df['% annual variation'] = new_df['Value'].pct_change() * 100
new_df.dropna(inplace=True)
X_axis = new_df.index
Y_axis = new_df["% annual variation"]

graph = px.line(y = Y_axis, x = X_axis)
graph.update_yaxes(title = "% annual variation\nCPI all items less food and energy ")
graph.update_xaxes(title = "time")

graph.show()

