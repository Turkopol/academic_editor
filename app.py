import streamlit as st
import language_tool_python
import textstat

tool = language_tool_python.LanguageTool('en-US')

st.set_page_config(page_title="Academic English Editor", layout="wide")
st.title("📘 Academic English Editor (Offline Version)")

text_input = st.text_area("Paste your academic English text below:", height=300)

if st.button("🔍 Analyze Text"):
    if text_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        st.subheader("✅ Grammar and Spelling Suggestions")
        matches = tool.check(text_input)
        if not matches:
            st.success("No issues found. Great job!")
        else:
            for match in matches:
                st.markdown(f"🔸 **{match.ruleId}** — {match.message}")
                st.markdown(f"• **Suggestion**: `{match.replacements}`")
                st.markdown(f"• **Context**: `{match.context}`")
                st.markdown("---")

        st.subheader("📊 Readability & Text Statistics")
        st.write(f"**Flesch Reading Ease**: {textstat.flesch_reading_ease(text_input)}")
        st.write(f"**Flesch-Kincaid Grade Level**: {textstat.flesch_kincaid_grade(text_input)}")
        st.write(f"**Gunning Fog Index**: {textstat.gunning_fog(text_input)}")
        st.write(f"**Dale-Chall Score**: {textstat.dale_chall_readability_score(text_input)}")
        st.write(f"**Word Count**: {textstat.lexicon_count(text_input)}")
        st.write(f"**Sentence Count**: {textstat.sentence_count(text_input)}")
