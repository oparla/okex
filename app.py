import streamlit as st
import pandas as pd

def get_transaction_history(url):
    try:
        df = pd.read_html(url)[0]  # Membaca tabel dari URL
        return df
    except Exception as e:
        st.error(f"Terjadi kesalahan dalam memuat tabel: {e}")
        return None

def main():
    st.title("Data Transaksi")

    url = "https://pgkreload.com/history"  # Ganti dengan URL yang sesuai
    df = get_transaction_history(url)

    if df is not None:
        st.write("Data Transaksi:")
        st.dataframe(df)
    else:
        st.warning("Tidak ada data transaksi yang tersedia.")

if __name__ == "__main__":
    main()
