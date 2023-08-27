import os
import streamlit as st
from pytube import YouTube
import base64

# Dynamically get the user's download directory
user_home = os.path.expanduser("~")
download_folder = os.path.join(user_home, "Downloads")

# Default audio file name
default_audio_name = "download.mp3"

def download_audio(youtube_url, audio_name=None):
    yt = YouTube(youtube_url)
    audio = yt.streams.get_audio_only()

    if audio_name:
        filename = audio_name
    else:
        filename = default_audio_name

    downloaded_file_path = audio.download(download_folder, filename=filename)
    return downloaded_file_path

def main():
    st.title("Vtube Music Downloader")
    url = st.text_input("Enter YouTube video link or URL", placeholder="https://youtu.be/idQ1n3cdgfo")

    if "yout" in url:
        # Ask for permission to download to download folder
        permission = st.checkbox(f"Do you give permission to download the audio file to {download_folder}?")
        
        if permission:
            try:
                downloaded_file_path = download_audio(url)

                with open(downloaded_file_path, "rb") as audio_file:
                    audio_data = audio_file.read()
                    audio_bytes = base64.b64encode(audio_data).decode("utf-8")

                st.audio(audio_data, format="audio/mp3")
                st.download_button("Download", data=audio_data, file_name=default_audio_name)
            except Exception as e:
                st.error("An error occurred during download or playback.")
                st.error(str(e))
        else:
            st.warning("You did not provide permission to download the file to your Downloads directory.")

if __name__ == "__main__":
    main()
