import streamlit as st
import requests

def get_all_orders(consumer_key, consumer_secret):
    url = "https://pgkteknologi.com/wp-json/wc/v3/orders"
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    data = response.json()
    return data

def main():
    st.title("Daftar Pesanan dari WooCommerce")
    
    consumer_key = "ck_1eab87430222326d0a5a0b92cf46c5b67077bd9b"
    consumer_secret = "cs_c5b1dfd2fce307faa6c91fe770b9fcd94cfcb341"
    
    try:
        orders = get_all_orders(consumer_key, consumer_secret)
        
        st.write("Jumlah Pesanan:", len(orders))
        
        for order in orders:
            st.write("Nomor Pesanan:", order["number"])
            st.write("Status:", order["status"])
            st.write("Total Harga:", order["total"])
            st.write("------------------------------")
    except requests.exceptions.RequestException as e:
        st.write("Terjadi kesalahan saat mengambil data pesanan:", e)

if __name__ == '__main__':
    main()
