import os 
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY_cypto')

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

import pandas as pd
pd.set_option('display.max_columns',None)
df= pd.json_normalize(data['data'])
df['time_stamp']= pd.to_datetime('now')
df

# with out creating csv
#def api_runner():
 # global df
  #url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  #parameters = {
    #'start':'1',
    #'limit':'15',
    #'convert':'USD'
  #}
  #headers = {
   # 'Accepts': 'application/json',
    #'X-CMC_PRO_API_KEY': API_KEY,
  #}

  #session = Session()
  #session.headers.update(headers)

  #try:
   # response = session.get(url, params=parameters)
    #data = json.loads(response.text)
    #data=list(data)
    #print(data)
  #except (ConnectionError, Timeout, TooManyRedirects) as e:
   # print(e)
  
  #pd.set_option('display.max_columns',None)
  #df2= pd.json_normalize(data['data'])
  #df2['time_stamp']=pd.to_datetime('now')

  #df = pd.concat([df, df2])

def api_runner():
  global df
  url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
  
  pd.set_option('display.max_columns',None)
  df= pd.json_normalize(data['data'])
  df['time_stamp']=pd.to_datetime('now')
  df
  
  if not os.path.isfile(r'C:\Users\tinka\Desktop\learning\Sheets\crypto API.csv'):
    df.to_csv(r'C:\Users\tinka\Desktop\learning\Sheets\crypto API.csv',header='column_names')
  else:
    df.to_csv(r'C:\Users\tinka\Desktop\learning\Sheets\crypto API.csv',mode='a',header=False)

from time import time
from time import sleep

for i in range (333):
  api_runner()
  print('api runner completed')
  sleep(60)
exit()

df= pd.read_csv(r'C:\Users\tinka\Desktop\learning\Sheets\crypto API.csv')
pd.set_option('display.float_format',lambda x:'%.5f' %x)
df

df2= df.groupby('name',sort=False)[['quote.USD.percent_change_1h', 
                               'quote.USD.percent_change_24h',	
                               'quote.USD.percent_change_7d',	
                               'quote.USD.percent_change_30d',
                               'quote.USD.percent_change_60d',	
                               'quote.USD.percent_change_90d'
                               ]].mean()

df2
df3=df2.stack()
df3

type(df3)
df4= df3.to_frame(name='values')
df4

pd.set_option('display.max_rows',None)
df4.reset_index(inplace=True)
df4=df4.rename(columns={'level_1':'percentage_change'})
df4['percentage_change']=df4['percentage_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h',	'quote.USD.percent_change_7d',	'quote.USD.percent_change_30d','quote.USD.percent_change_60d',	'quote.USD.percent_change_90d'], ['1h','24h','7d','30d','60d','90d'])
#df4.set_index(['name','percentage_change'], inplace=True)


import seaborn as sms
import matplotlib.pyplot as plt

sms.catplot(x='percentage_change',y='values',hue='name',data=df4,kind='point')

#df5= df2.transpose()
#df5
#df5.reset_index(inplace=True)
#df6= df5.rename(columns={'index':'percentage_change'},)
#df6
