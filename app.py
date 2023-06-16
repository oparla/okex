import streamlit as st
import requests
import json
from datetime import datetime

def get_visitor_details(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def main():
    st.title("Detail Pengunjung")

    # Mendapatkan alamat IP pengunjung
    ip = st.experimental_get_query_params().get("ip", [None])[0]

    if ip:
        st.write(f"Alamat IP: {ip}")

        # Mendapatkan detail pengunjung berdasarkan alamat IP
        visitor_data = get_visitor_details(ip)
        st.write("Detail Pengunjung:")
        st.write(f"Negara: {visitor_data.get('country')}")
        st.write(f"Kota: {visitor_data.get('city')}")
        st.write(f"Koordinat: {visitor_data.get('loc')}")
        st.write(f"Zona Waktu: {visitor_data.get('timezone')}")
        st.write(f"Penyedia Layanan Internet: {visitor_data.get('org')}")
        st.write(f"Hostname: {visitor_data.get('hostname')}")

        # Menyimpan data kunjungan pengunjung ke file log
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("visitor_log.txt", "a") as f:
            f.write(f"{timestamp} - IP: {ip} - Negara: {visitor_data.get('country')}\n")
    else:
        st.warning("Tidak dapat mendapatkan alamat IP pengunjung.")

if __name__ == "__main__":
    main()
