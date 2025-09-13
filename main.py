import streamlit as st
import scrape as sc

st.title("AI Web Scraper")

url=st.text_input("Enter a Website URL:")

if(st.button("Scrape Site")):
    st.write("Scrapping the site")
    result=sc.scrape_website(url)
    body_content=sc.extract_body_content(result)
    cleaned_content=sc.clean_body_content(body_content)

    st.session_state.dom_content=cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)