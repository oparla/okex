import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

class CameraTransformer(VideoTransformerBase):
    def transform(self, frame):
        return frame

def main():
    st.title("Tampilan Kamera Streamlit")

    webrtc_streamer(key="example", video_transformer_factory=CameraTransformer)

if __name__ == "__main__":
    main()
