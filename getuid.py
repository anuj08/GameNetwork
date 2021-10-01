import requests
import time
import pandas as pd

url = "https://steamspy.com/api.php"
parameters = {"request": "all"}
json_data = requests.get(url,parameters).json()
steam_spy_all = pd.DataFrame.from_dict(json_data, orient='index')
app_list = steam_spy_all[['appid', 'name']].sort_values('appid').reset_index(drop=True)

app_list.to_csv('app_list.csv', index=False)
