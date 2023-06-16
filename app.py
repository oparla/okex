import streamlit as st
import pandas as pd
import requests

def get_transaction_history():
    url = "https://pgkreload.com/history"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    st.title("Data Transaksi")

    # Mendapatkan data transaksi
    transaction_data = get_transaction_history()

    if transaction_data:
        # Menyusun data transaksi menjadi DataFrame
        df = pd.DataFrame(transaction_data)

        st.write("Data Transaksi:")
        st.dataframe(df)
    else:
        st.warning("Tidak ada data transaksi yang tersedia.")

if __name__ == "__main__":
    main()
