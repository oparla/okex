import streamlit as st
import requests

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data[coin]['usd']
    return price

def main():
    st.title("Harga BCD dan BAT")
    bcd_price = get_price('bitcoin-diamond')
    bat_price = get_price('basic-attention-token')
    
    st.write("Harga Bitcoin Diamond (BCD): $", bcd_price)
    st.write("Harga Basic Attention Token (BAT): $", bat_price)

if __name__ == '__main__':
    main()
