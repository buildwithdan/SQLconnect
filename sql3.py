import requests
import pandas as pd
import numpy as np

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
    for page in range(41):
        url = f"https://www.rightmove.co.uk/api/_search?locationIdentifier=REGION%{borough_code}&numberOfPropertiesPerPage=100&radius=0.0&sortType=2&index={str(24*page)}&maxBedrooms=3&minBedrooms=2&maxPrice=550000&minPrice=475000&sortType=6&propertyTypes=&includeSSTC=false&viewType=LIST&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false"
        print(f'Scraping: {name} - Page: {page}')
        data = requests.get(url,headers=headers).json()
        properties = data['properties']
        output.extend(properties)

df = pd.json_normalize(output)

#df.to_csv('scraped_data.csv',index=False)

connection = psycopg2.connect(user="dnellpersonal",
                                  password="v2_3uywZ_D7WHHVhxkSCDwhHLvFj9CZ9",
                                  host="db.bit.io",
                                  port="5432",
                                  database="dnellpersonal/test1")

cursor = connection.cursor()

df.to_sql('rightmove', connection)

    #postgres_insert_query = """ INSERT INTO rightmove VALUES (%s,%s,%s,%s)"""
    #record_to_insert = ('www.google.com', '6 Birch Tree Way','2bedroom with a pug',320000)
    #cursor.execute(postgres_insert_query, record_to_insert)

connection.commit()
count = cursor.rowcount