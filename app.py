import streamlit as st
import pandas as pd

# Import library untuk melakukan HTTP request
import requests
from bs4 import BeautifulSoup

# Fungsi untuk melakukan scraping dan mengambil data tabel
def scrape_table(url):
    # Mengirim HTTP GET request ke URL
    response = requests.get(url)
    
    # Mengecek status code response
    if response.status_code == 200:
        # Membuat objek BeautifulSoup untuk melakukan parsing HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Mencari tabel berdasarkan class
        table = soup.find('table', class_='table table-striped')
        
        # Membaca tabel dan mengkonversikannya menjadi DataFrame
        df = pd.read_html(str(table))[0]
        
        return df
    else:
        st.error(f'Error: {response.status_code}')

# URL yang akan di-scrape
url = 'https://pgkreload.com/history'

# Melakukan scraping dan mengambil data tabel
table_data = scrape_table(url)

# Menampilkan data tabel menggunakan Streamlit
st.table(table_data)
