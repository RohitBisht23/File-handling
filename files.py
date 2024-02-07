import streamlit as st
import pandas as pd

st.subheader('Uploading the csv files ')

df = st.file_uploader('Uploading the scv file', type=['csv','xlsx'])

# if(df is not None) :
#     st.dataframe(df)
st.subheader('Loading the csv files ')
df = pd.read_csv('apparel.csv', encoding='latin1')
if df is not None:
    st.table(df.head())


#Image uploading
st.subheader('Dealing with images')
img = st.file_uploader('Uploading the scv file', type=['png','jpg','jpeg'])
if img is not None:
    st.image(img)

st.image("porfolio.jpg")
    

#Working with video file
st.subheader('Working with video file')
video_file = st.file_uploader('Upload the video :',type=['mkv','mp4'])
if video_file is not None:
    st.video(video_file)

st.video("WhatsApp Video 2023-10-18 at 23.31.40_572fe237.mp4")


#Working with audio file
st.subheader('Working with audio file')
audio_file = st.file_uploader('Upload the video :',type=['mp3','wva'])
if video_file is not None:
    st.video(audio_file)
