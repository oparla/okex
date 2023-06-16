import streamlit as st
import requests

def get_indodax_price(pair):
    url = f'https://indodax.com/api/ticker/{pair}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['ticker']['last']
    else:
        st.error(f'Error: {response.status_code}')
        return None

# Mendapatkan harga BAT dan BCD
bat_price = get_indodax_price('batidr')
bcd_price = get_indodax_price('bcdidr')

# Menampilkan harga menggunakan Streamlit
if bat_price is not None:
    st.write('Harga BAT (Basic Attention Token) di Indodax:')
    st.write(f'IDR {bat_price}')

if bcd_price is not None:
    st.write('Harga BCD (Bitcoin Diamond) di Indodax:')
    st.write(f'IDR {bcd_price}')
