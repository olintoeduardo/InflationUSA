import pandas as pd
import plotly.express as px
import plotly.graph_objects as go




allitems_csv = "allitems.csv"
gasoline_csv = "gasoline.csv"

#Using the parameters to consider the dataset as time series
allitems_df = pd.read_csv(allitems_csv, parse_dates=["Label"], index_col= "Label")
gasoline_df = pd.read_csv(gasoline_csv, parse_dates=["Label"], index_col= "Label")

#Extracting from only 1967 onwards 
allitems_df = allitems_df[allitems_df.Year >= 1967]


#transform the monthly frequency into yearly, getting the last day of the month.
allitems_annual_df = allitems_df.resample('A').last()
gasoline_annual_df = gasoline_df.resample('A').last()
print(allitems_annual_df)
#calculating the percentage change from the last day of the month of a year to the next
allitems_annual_df['% annual variation all items'] = allitems_annual_df['Value'].pct_change() * 100
gasoline_annual_df['% annual variation gasoline'] = gasoline_annual_df['Value'].pct_change() * 100


# #dropping the first row which contains Nan data because of the 1966 values.
allitems_annual_df.dropna(inplace=True)
gasoline_annual_df.dropna(inplace=True)


all_df = pd.merge(allitems_annual_df,gasoline_annual_df,on = "Label",how = "left")

#Cleaning up remaining dataset
all_df = all_df.drop(["Year_y","Period_y","Series ID_y"], axis = "columns")
all_df = all_df.drop(["Year_x","Period_x","Series ID_x"], axis = "columns")

#preparing the graph
X_axis = all_df.index
Y_allitems = all_df["% annual variation all items"]
Y_gasoline = all_df["% annual variation gasoline"]

fig = go.Figure()
fig.add_trace(go.Scatter(x=X_axis, y=Y_gasoline,
                    mode='lines',
                    name='gasoline'))
fig.add_trace(go.Scatter(x=X_axis, y=Y_allitems,
                    mode='lines',
                    name='all items'))

fig.update_layout(title='CPI All items vs gasoline % annual variation vs time',
                   xaxis_title='Time',
                   yaxis_title='CPI All items vs gasoline % annual variation since 1967')


# #plotting the graph
fig.show()

