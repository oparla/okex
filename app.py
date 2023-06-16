import streamlit as st
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
        st.write("Data Transaksi:")
        for transaction in transaction_data:
            st.write(f"ID Transaksi: {transaction.get('id')}")
            st.write(f"Tanggal: {transaction.get('date')}")
            st.write(f"Keterangan: {transaction.get('description')}")
            st.write(f"Jumlah: {transaction.get('amount')}")
            st.write("--------------------")
    else:
        st.warning("Tidak ada data transaksi yang tersedia.")

if __name__ == "__main__":
    main()
