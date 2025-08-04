import streamlit as st
import textstat

st.set_page_config(page_title="Academic English Analyzer", layout="wide")
st.title("📘 Academic Text Analyzer (Cloud-Friendly Version)")

text_input = st.text_area("Paste your academic English text below:", height=300)

if st.button("🔍 Analyze Text"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.subheader("📊 Readability & Text Statistics")
        st.write(f"**Flesch Reading Ease**: {textstat.flesch_reading_ease(text_input)}")
        st.write(f"**Flesch-Kincaid Grade Level**: {textstat.flesch_kincaid_grade(text_input)}")
        st.write(f"**Gunning Fog Index**: {textstat.gunning_fog(text_input)}")
        st.write(f"**Dale-Chall Score**: {textstat.dale_chall_readability_score(text_input)}")
        st.write(f"**Word Count**: {textstat.lexicon_count(text_input)}")
        st.write(f"**Sentence Count**: {textstat.sentence_count(text_input)}")
