import os
import streamlit as st
import yt_dlp

# Dynamically get the user's download directory
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Default names
default_audio_name = "download_2023.mp3"
default_video_name = "download.mp4"

def download_audio(youtube_url, audio_name=default_audio_name):
    output_filename = f"{audio_name}.%(ext)s"
    
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': os.path.join(download_folder, output_filename),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([youtube_url])
    
    return os.path.join(download_folder, output_filename.replace('%(ext)s', 'mp3'))



def main():
    st.title("Vtube Music Downloader")
    url = st.text_input("Enter YouTube video link or URL", placeholder="https://youtu.be/idQ1n3cdgfo")

    if "yout" in url:
        permission = st.checkbox(f"Do you give permission to download the audio file to {download_folder}?")
        
        if permission:
            try:
                downloaded_file_path = download_audio(url)
                
                with open(downloaded_file_path, "rb") as audio_file:
                    audio_data = audio_file.read()
                
                st.download_button("Download", data=audio_data, file_name=default_audio_name)
            except Exception as e:
                st.error(f"An error occurred: {e}")

        else:
            st.warning("You did not provide permission to download the file to your Downloads directory.")

if __name__ == "__main__":
    main()
