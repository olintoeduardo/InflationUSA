import pandas as pd

#IMPORTING CSV AND DROPPING UNNECESSARY COLUMNS
#csv string declarations
allitems_csv = "allitems.csv"
allitems_foodenergy_csv = "allitems_foodenergy.csv"
gasoline_csv = "gasoline.csv"

#importing data from csv files, treating as time series
allitems_df = pd.read_csv(allitems_csv, parse_dates=["Label"])
allitems_foodenergy_df = pd.read_csv(allitems_foodenergy_csv, parse_dates=["Label"])
gasoline_df = pd.read_csv(gasoline_csv, parse_dates=["Label"])


allitems_df = allitems_df.drop(["Year","Period","Series ID"], axis = "columns")
allitems_foodenergy_df = allitems_foodenergy_df.drop(["Year","Period","Series ID"], axis = "columns")
gasoline_df = gasoline_df.drop(["Year","Period","Series ID"], axis = "columns")
# allitems_df

'''Discussion: as the file containing CPI for All items, seasonally adjusted has records
from 1947 onwards, we will use its Label column as the main one. The file containing CPI 
for All items less food and energy, seasonally adjusted has records from 1957 onwards, and 
CPI Gasoline, seasonally adjusted from 1967 onwards. Thus, I will insert NaN values in the
Value column, where those two files don't have any records.

'''
#Merge operation first all items/less food and energy on all items.
new_df = pd.merge(allitems_df, allitems_foodenergy_df, on='Label', how='left')
#Merge operation now gasoline on the previous dataframe.
new_df = pd.merge(new_df, gasoline_df, on='Label', how='left')

#Renaming columns for better readability
new_df.rename(columns = {"Label":"Month","Value_x":"All items","Value_y":"All items/less food&energy", "Value":"Gasoline"}, inplace = True)
# new_df

#Saving dataframe to CSV file
new_df.to_csv("InflationUSA.csv",index=False)