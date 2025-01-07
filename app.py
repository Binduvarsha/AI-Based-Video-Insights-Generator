import streamlit as st
import os
from src.video_info import GetVideo
from src.model import Model
from src.prompt import Prompt
from src.misc import Misc
from src.timestamp_formatter import TimestampFormatter
from src.copy_module_edit import ModuleEditor
from dotenv import load_dotenv
from st_copy_to_clipboard import st_copy_to_clipboard

class AIVideoSummarizer:
    def __init__(self):
        self.youtube_url = None
        self.video_id = None
        self.video_title = None
        self.video_transcript = None
        self.video_transcript_time = None
        self.summary = None
        self.time_stamps = None
        self.transcript = None
        self.col1 = None
        self.col2 = None
        self.model_name = "Gemini"  # Set to Gemini by default
        load_dotenv()

    def get_youtube_info(self):
        self.youtube_url = st.text_input("Enter YouTube Video Link")

        # Check for Gemini API Key
        if not os.getenv("GOOGLE_GEMINI_API_KEY"):
            st.warning('Error: Google Gemini API key not found in environment variables.', icon="⚠️")

        if self.youtube_url:
            self.video_id = GetVideo.Id(self.youtube_url)
            if self.video_id is None:
                st.write("**Error**")
                st.image("https://i.imgur.com/KWFtgxB.png", use_column_width=True)
                st.stop()
            self.video_title = GetVideo.title(self.youtube_url)
            st.write(f"**{self.video_title}**")
            st.image(f"http://img.youtube.com/vi/{self.video_id}/0.jpg", use_column_width=True)

    def generate_summary(self):
        if st.button(":rainbow[**Get Summary**]"):
            self.video_transcript = GetVideo.transcript(self.youtube_url)
            if self.video_transcript:
                self.summary = Model.google_gemini(transcript=self.video_transcript, prompt=Prompt.prompt1())
                st.markdown("## Summary:")
                st.write(self.summary)
                st_copy_to_clipboard(self.summary)
            else:
                st.error("Failed to retrieve video transcript.")

    def generate_time_stamps(self):
        if st.button(":rainbow[**Get Timestamps**]"):
            self.video_transcript_time = GetVideo.transcript_time(self.youtube_url)
            youtube_url_full = f"https://youtube.com/watch?v={self.video_id}"
            if self.video_transcript_time:
                self.time_stamps = Model.google_gemini(self.video_transcript_time, Prompt.prompt1(ID='timestamp'), extra=youtube_url_full)
                st.markdown("## Timestamps:")
                st.markdown(self.time_stamps)
                cp_text = TimestampFormatter.format(self.time_stamps)
                st_copy_to_clipboard(cp_text)
            else:
                st.error("Failed to retrieve video transcript time.")

    def generate_transcript(self):
        if st.button("Get Transcript"):
            self.video_transcript = GetVideo.transcript(self.youtube_url)
            self.transcript = self.video_transcript
            if self.transcript:
                st.markdown("## Transcript:")
                st.download_button(label="Download as text file", data=self.transcript, file_name=f"Transcript - {self.video_title}")
                st.write(self.transcript)
                st_copy_to_clipboard(self.transcript)
            else:
                st.error("Failed to retrieve video transcript.")

    def run(self):
        st.set_page_config(page_title="AI Video Summarizer", page_icon="chart_with_upwards_trend", layout="wide")
        st.title("AI-Based Videos Insights Generator")
        editor = ModuleEditor('st_copy_to_clipboard')
        editor.modify_frontend_files()

        self.col1, self.col2, self.col3 = st.columns(3)

        with self.col1:
            self.get_youtube_info()

        ran_loader = Misc.loaderx() 
        n, loader = ran_loader[0], ran_loader[1]

        with self.col3:
            mode = st.radio(
                "What do you want to generate for this video?",
                [":rainbow[**AI Summary**]", ":rainbow[**AI Timestamps**]", "**Transcript**"],
                index=0)
            if mode == ":rainbow[**AI Summary**]":
                with st.spinner(loader[n]):
                    self.generate_summary()
            elif mode == ":rainbow[**AI Timestamps**]":
                with st.spinner(loader[n]):
                    self.generate_time_stamps()
            else:
                with st.spinner(loader[0]):
                    self.generate_transcript()

        # st.write(Misc.footer(), unsafe_allow_html=True)
        st.write(Misc.ind(), unsafe_allow_html=True)


if __name__ == "__main__":
    app = AIVideoSummarizer()
    app.run()
