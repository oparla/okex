import streamlit as st
import time

# Fungsi untuk menampilkan balon berulang-ulang
def display_balloons():
    st.balloons()
    time.sleep(1)  # Jeda 1 detik
    display_balloons()  # Memanggil kembali fungsi display_balloons untuk membuat balon berulang-ulang

# Memanggil fungsi display_balloons untuk memulai animasi balon
display_balloons()
