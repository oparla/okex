import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, RTCConfiguration

class CameraTransformer(VideoTransformerBase):
    def transform(self, frame):
        return frame

def main():
    st.title("Tampilan Kamera Streamlit")

    # Konfigurasi RTC (Real-Time Communication)
    rtc_configuration = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    # Menampilkan perangkat yang tersedia jika URL diakses oleh pengunjung
    if st.button("Tampilkan Perangkat"):
        devices = webrtc_streamer.get_all_devices()
        st.write("Perangkat yang tersedia:")
        for device in devices:
            st.write(device)

    # Mengizinkan akses kamera jika pengunjung mengizinkannya
    webrtc_streamer(
        key="example",
        video_transformer_factory=CameraTransformer,
        rtc_configuration=rtc_configuration,
        async_transform=True,
    )

if __name__ == "__main__":
    main()
