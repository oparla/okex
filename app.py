import streamlit as st

def main():
    # Mendefinisikan latitude dan longitude
    latitude = -2.9760735
    longitude = 104.7754307

    # Membuat URL Google Maps dengan parameter latitude dan longitude
    maps_url = f"https://www.google.com/maps?q={latitude},{longitude}&z=15&output=embed"

    # Menampilkan peta Google Maps di Streamlit
    st.markdown(f'<iframe src="{maps_url}" width="1000" height="500"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
