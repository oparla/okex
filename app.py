import streamlit as st
import time

# Fungsi untuk membuat animasi balon meledak
def explode_balloon():
    balloon = st.balloons()
    time.sleep(2)  # Jeda 2 detik untuk menampilkan balon
    st.balloons(balloon)  # Menampilkan balon meledak

# Memanggil fungsi explode_balloon untuk memulai animasi meledak
explode_balloon()
