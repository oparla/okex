import streamlit as st
import requests

def get_price(coin, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    price = data[coin][currency]
    return price

def main():
    st.title("Harga BCD dan BAT")
    
    currency = "idr"  # Ubah sesuai dengan kode mata uang yang kamu inginkan
    
    bcd_price = get_price('bitcoin-diamond', currency)
    bat_price = get_price('basic-attention-token', currency)
    
    st.write("Harga Bitcoin Diamond (BCD):", currency.upper(), bcd_price)
    st.write("Harga Basic Attention Token (BAT):", currency.upper(), bat_price)

if __name__ == '__main__':
    main()
