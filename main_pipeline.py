import streamlit as st
from src.api.youtube_api import get_video_details
from src.data.preprocess import clean_text
from src.nlp.sentiment_analysis import analyze_sentiment
from src.nlp.summarization import summarize_text
from dotenv import load_dotenv
import os

# โหลดค่าในไฟล์ .env
load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

# ฟังก์ชันประมวลผลลิงก์ YouTube
def process_youtube_link(video_id):
    details = get_video_details(API_KEY, video_id)
    description = details['items'][0]['snippet']['description']
    clean_description = clean_text(description)
    sentiment_result = analyze_sentiment(clean_description)
    summary = summarize_text(clean_description)
    return {
        "title": details['items'][0]['snippet']['title'],
        "clean_description": clean_description,
        "sentiment": sentiment_result,
        "summary": summary,
        "view_count": details['items'][0]['statistics']['viewCount']
    }

# อินเทอร์เฟซของ Streamlit
st.title("YouTube Video Summary and Analysis")
youtube_link = st.text_input("Enter YouTube video link:")

if st.button("Analyze"):
    if youtube_link:
        try:
            video_id = youtube_link.split("v=")[-1]
            result = process_youtube_link(video_id)
            st.subheader("Video Title")
            st.write(result["title"])
            st.subheader("Summary")
            st.write(result["summary"])
            st.subheader("Sentiment Analysis")
            st.write(result["sentiment"])
            st.subheader("View Count")
            st.write(result["view_count"])
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube link.")


