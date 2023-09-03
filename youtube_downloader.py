import os
import streamlit as st
import base64
import yt_dlp
import imageio_ffmpeg as ffmpeg

# Dynamically get the user's download directory
user_home = os.path.expanduser("~")
download_folder = os.path.join(user_home, "Downloads")

# Default audio file name
default_audio_name = "download_2023.mp3"



# import os
# import imageio_ffmpeg as ffmpeg


def download_audio(youtube_url, audio_name=None):
    if audio_name:
        output_filename = f"{audio_name}.%(ext)s"
    else:
        output_filename = f"{default_audio_name}.%(ext)s"
    
    options = {
        'format': 'bestaudio/best',
        'outtmpl': f"{download_folder}/{output_filename}"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        # The full path to the downloaded file
        file_path = ydl.prepare_filename(info_dict)

    return file_path






def main():
    st.title("Vtube Music Downloader")
    url = st.text_input("Enter YouTube video link or URL", placeholder="https://youtu.be/idQ1n3cdgfo")

    if "yout" in url:
        # Ask for permission to download to download folder
        permission = st.checkbox(f"Do you give permission to download the audio file to {download_folder}?")
        
        if permission:
            try:
                downloaded_file_path = download_audio(url)
                # video_path = download_video(url)

                with open(downloaded_file_path, "rb") as audio_file:
                    audio_data = audio_file.read()
                    # audio_bytes = base64.b64encode(audio_data).decode("utf-8")

                # st.audio(audio_data, format="audio/mp3")
                # st.video(video_path)
                st.download_button("Download", data=audio_data, file_name=default_audio_name)
            except Exception as e:
                st.error("An error occurred during download or playback.")
                st.error(str(e))
        else:
            st.warning("You did not provide permission to download the file to your Downloads directory.")

if __name__ == "__main__":
    main()
