'''
Scrapping dilakukan pada webiste https://app.jala.tech/harga_udang#size=100

'''



import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def fetch_page(page):
    url = f'https://app.jala.tech/api/shrimp_prices?page={page}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data['data'])
        return df
    else:
        print(f"Failed to retrieve data from page {page}")
        return pd.DataFrame()  

all_data = []

with ThreadPoolExecutor(max_workers=10) as executor:
    pages = list(range(1, 416))
    
    results = executor.map(fetch_page, pages)
    
    all_data = list(results)

final_df = pd.concat(all_data, ignore_index=True)

print(final_df)
final_df.to_csv('shrimp_prices.csv', index=False)