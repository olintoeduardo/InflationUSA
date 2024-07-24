import requests
import json
import pandas as pd

#the following code is available in the BLS website and I just adapted to read the data into a pandas dataframe
#the api key was generated to my email
api_key = "936de0fc206c45178a9f3bd5cf78a6af"

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0'],"startyear":"2005","endyear":"2024","registrationkey": api_key})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/',data=data, headers=headers)
json_data = json.loads(p.text)
print(json_data)
structured_data = []
for series in json_data['Results']['series']:
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        if 'M01' <= period <= 'M12':
            structured_data.append({'year':year,'period':period,'value':value})

data = pd.DataFrame(structured_data)
print(data)