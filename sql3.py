import requests
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine

#define variables, could add others for maxPrice etc

#https://www.reddit.com/r/webscraping/comments/wjb8uv/rightmove_scraping/
#https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=London&useLocationIdentifier=true&locationIdentifier=REGION%5E87490&buy=For+sale


boroughs = {
    "City of London": "5E61224"
}

# define our user headers
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}


output = []
for name,borough_code in boroughs.items():
    for page in range(5):
        url = f"https://www.rightmove.co.uk/api/_search?locationIdentifier=REGION%{borough_code}&numberOfPropertiesPerPage=100&radius=0.0&sortType=2&index={str(24*page)}&maxBedrooms=3&minBedrooms=2&maxPrice=550000&minPrice=475000&sortType=6&propertyTypes=&includeSSTC=false&viewType=LIST&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false"
        print(f'Scraping: {name} - Page: {page}')
        data = requests.get(url,headers=headers).json()
        properties = data['properties']
        output.extend(properties)

df = pd.json_normalize(output)

#df.to_csv('scraped_data.csv',index=False)

conn_string = 'postgresql://r00t:thebuckstopshere!!@192.168.1.206/PropertyData'
  
db = create_engine(conn_string)
conn = db.connect()

df.to_sql('example1', conn, if_exists='replace',index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()