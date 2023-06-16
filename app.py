import streamlit as st
import requests
import locale

def get_price(coin, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    price = data[coin][currency]
    return price

def format_currency(price):
    locale.setlocale(locale.LC_ALL, 'id_ID')  # Setel lokalisasi ke bahasa Indonesia
    formatted_price = locale.currency(price, grouping=True)
    return formatted_price

def main():
    st.title("Harga BCD dan BAT")
    
    currency = "idr"  # Ubah sesuai dengan kode mata uang yang kamu inginkan
    
    try:
        bcd_price = get_price('bitcoin-diamond', currency)
        bat_price = get_price('basic-attention-token', currency)
        
        formatted_bcd_price = format_currency(bcd_price)
        formatted_bat_price = format_currency(bat_price)
        
        st.write("Harga Bitcoin Diamond (BCD):", formatted_bcd_price)
        st.write("Harga Basic Attention Token (BAT):", formatted_bat_price)
    except KeyError:
        st.write("Tidak dapat memperoleh data harga saat ini.")

if __name__ == '__main__':
    main()
