import streamlit as st
import time

# Menampilkan animasi balon
st.balloons()

# Memberikan jeda selama 2 detik sebelum menampilkan balon meledak
time.sleep(2)

# Menghapus animasi balon
st.balloons(0)
