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

    # Mengizinkan akses kamera pengunjung dari perangkat seluler saja
    video_transformer_factory = None if st.button("Izinkan Kamera") else CameraTransformer

    # Menampilkan tampilan kamera pengunjung di web desktop
    webrtc_streamer(
        key="example",
        video_transformer_factory=video_transformer_factory,
        rtc_configuration=rtc_configuration,
        async_transform=True,
    )

if __name__ == "__main__":
    main()
