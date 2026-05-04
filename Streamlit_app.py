import streamlit as st
from fetch_news import get_news
from process_news import process_news
from search_news import search_news


st.title("📰 News Agent App")


raw_data = get_news()

if not raw_data:
    st.error("Failed to fetch news")
    st.stop()

news_list = process_news(raw_data)


keyword = st.text_input("🔍 Search News")


if keyword:
    filtered_news = search_news(news_list, keyword)
else:
    filtered_news = news_list


st.subheader("Top News")

for news in filtered_news[:10]:
    st.markdown(f"### {news['title']}")
    
    if news["description"]:
        st.write(news["description"])
    
    st.markdown(f"[Read More]({news['url']})")
    st.markdown("---")