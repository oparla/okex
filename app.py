import streamlit as st

# URL video YouTube
video_url = "https://www.youtube.com/watch?v=lXM1igUSkJM&pp=ygUGdGhvbWFz"

# Menampilkan video dari YouTube dalam mode layar penuh dengan pemutaran otomatis
st.video(video_url, start_time=0, format='auto', start_paused=True)

# Mengubah tata letak aplikasi menjadi layar penuh
st.markdown('<style>body{margin: 0;}</style>', unsafe_allow_html=True)
