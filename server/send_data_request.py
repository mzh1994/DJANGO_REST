import pandas as pd
import requests
import json

file = r'C:\Users\M ZOHAIB HASSAN\Desktop\HUBCO\1. Database\4. Sample_readings_data_input_table.xlsx'
df = pd.read_excel(file).head(2)
#data = df.to_dict()
#data = df.to_dict('records')
data = [{"date": "Thu Jul 22 2021 13:49:35 GMT+0500 (PKT)", "kks": "10LCB11CT307", "remarks": "All Okay","value": 78},
        {"date": "Thu Jul 22 2021 14:40:36 GMT+0500 (PKT)", "kks": "10LCB11CT307", "remarks": "hj", "value": 58}]
# data = [{'kks': '10GBB20CF101', 'date': '2021-07-11 00:00:54', 'value': 100, 'remarks': 'ok'},
#         {'kks': '10GBB20CL101', 'date': '2021-07-11 01:00:54', 'value': 90, 'remarks': 'ok'}]
url = "https://dataloggingapp.herokuapp.com/post_data"
#url = "http://localhost:8000/post_data"
headers = {'content-type': 'application/json'}
r=requests.post(url, data=json.dumps(data),headers = headers)
if len(r.text)<100:
    print(r.text)

# sample_data_from_android = {'kks': {0: '10GBB20CF101', 1: '10GBB20CL101', 2: '10GBB20CQ101', 3: '10GBB30CF101'},
#                             'date': {0: '2021-07-11 00:00:54', 1: '2021-07-11 01:00:54',
#                                     2: '2021-07-11 10:00:54', 3: '2021-07-11 00:00:54'},
#                             'value': {0: 100, 1: 90, 2: 67, 3: 445}, 
#                             'remarks': {0: 'ok', 1: 'ok', 2: 'Not ok', 3: 'Not ok'}}
# data = [{'kks': '10GBB20CF101', 'date': '2021-07-11 00:00:54', 'value': 100, 'remarks': 'ok'},
#                            {'kks': '10GBB20CL101', 'date': '2021-07-11 01:00:54', 'value': 90, 'remarks': 'ok'}, 
#                            {'kks': '10GBB20CQ101', 'date': '2021-07-11 10:00:54', 'value': 67, 'remarks': 'Not ok'},
#                            {'kks': '10GBB30CF101', 'date': '2021-07-11 00:00:54', 'value': 445, 'remarks': 'Not ok'}]

# data_lst = []
# for record in df.itertuples():
# 	data_lst.append(record)

# print(data_lst[0].kks)
