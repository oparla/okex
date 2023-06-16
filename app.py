import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_table(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')

        # Mengambil judul kolom
        header_row = rows[0]
        headers = [header.get_text(strip=True) for header in header_row.find_all('th')]

        # Mengambil data baris
        data_rows = rows[1:]
        data = []
        for row in data_rows:
            cells = row.find_all('td')
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)

        # Membuat DataFrame dari data tabel
        df = pd.DataFrame(data, columns=headers)
        return df
    else:
        st.error(f'Error: {response.status_code}')
        return None

url = 'https://pgkreload.com/history'
table_data = scrape_table(url)

if table_data is not None:
    st.table(table_data)
