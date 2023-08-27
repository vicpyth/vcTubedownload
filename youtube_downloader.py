from pytube import YouTube
import os
import streamlit as st
import base64



def downloder(youtube_url, audio_name=None,name="download.mp3"):
    audio = YouTube(youtube_url).streams.get_audio_only()
    if audio_name:
        name  = audio_name
        if os.path.exists(r"C:/Users/Acer/Desktop/VICTOR2023/down/download.mp3"):
            file_ = True
        else:
            file_ = False
        
        return audio.download("down",filename=name), file_
    else:
        name = name
    
        if os.path.exists(r"C:/Users/Acer/Desktop/VICTOR2023/down/download.mp3"):
            file_ = True
        else:
            file_ = False
    
        return audio.download("down",filename=name), file_


   

# C:\Users\Acer\Desktop\VICTOR2023\youtube_downloader.py

# downloder("https://www.youtube.com/watch?v=mqSQvoinDE4")
def main():
    st.title("Vtube music Downloader")
    url = st.text_input("Enter Youtube's video link or url", placeholder="https://www.youtube.com/watch?v=mqSQvoinDE4")
    file_name = r'C:\Users\Acer\Desktop\VICTOR2023\down\download.mp3'
    if "youtube" in url:
        st.text(url)
        _, file_ = downloder(url)
        if file_:
            
            
            with open(file_name, "rb") as audio_file:
                audio_data = audio_file.read()
                audio_bytes = base64.b64encode(audio_data).decode("utf-8")

            st.audio(audio_data, format="audio/mp3")
            st.download_button("Download", data=audio_data, file_name="download.mp3")
        else:
            "nope, try again"
        



if __name__ == "__main__":
    main()