import streamlit as st
import time

# Menampilkan animasi balon
balloon = st.balloons()

# Memberikan jeda selama 2 detik sebelum menampilkan balon meledak
time.sleep(2)

# Menampilkan balon meledak
st.balloons(balloon)
