import streamlit as st
import requests

def get_all_products(consumer_key, consumer_secret):
    url = "https://pgkteknologi.com/wp-json/wc/v3/products"
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    data = response.json()
    return data

def main():
    st.title("Daftar Produk dari WooCommerce")
    
    consumer_key = "ck_1eab87430222326d0a5a0b92cf46c5b67077bd9b"
    consumer_secret = "cs_c5b1dfd2fce307faa6c91fe770b9fcd94cfcb341"
    
    try:
        products = get_all_products(consumer_key, consumer_secret)
        
        st.write("Jumlah Produk:", len(products))
        
        for product in products:
            st.write("Nama Produk:", product["name"])
            st.write("Harga:", product["regular_price"])
            st.write("Deskripsi:", product["description"])
            st.write("------------------------------")
    except requests.exceptions.RequestException as e:
        st.write("Terjadi kesalahan saat mengambil data produk:", e)

if __name__ == '__main__':
    main()
