import streamlit as st
from textblob import TextBlob

st.title("Restaurant Review Sentiment Analysis")

review = st.text_area("Enter your review")

if st.button("Analyze"):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    
    st.write("Sentiment Score:", polarity)
    
    if polarity > 0.2:
        st.success("Positive 😊")
    elif polarity < -0.2:
        st.error("Negative 😡")
    else:
        st.warning("Neutral 😐")