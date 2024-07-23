import requests
import json
import pandas as pd
api_key = "936de0fc206c45178a9f3bd5cf78a6af"
startYear = 2005
endYear = 2024
allData = pd.DataFrame()
# while endYear <= 2024:
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0'],"startyear":str(startYear),"endyear":str(endYear),"registrationkey": api_key})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/',data=data, headers=headers)
json_data = json.loads(p.text)
print(json_data)
structured_data = []
for series in json_data['Results']['series']:
    # x=prettytable.PrettyTable(["series id","year","period","value",])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        if 'M01' <= period <= 'M12':
            structured_data.append({'year':year,'period':period,'value':value})

data = pd.DataFrame(structured_data)
    # allData = pd.concat([allData,data])
    # startYear = endYear + 1
    # endYear = endYear + 2

print(data)