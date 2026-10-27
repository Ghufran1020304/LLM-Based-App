import streamlit as st
from main import build_evidence, ask_llm

st.set_page_config(page_title="CNC Part Analysis", page_icon="🔧")
st.title("🔧 LLM-Based CNC Part Analysis")
st.caption("Level 1: Excel manufacturing record + LLM. Every answer names its source.")

part = st.text_input("Part number", value="2280")

if part:
    evidence = build_evidence(part.strip())
    if evidence is None:
        st.error(f"Part {part} was not found in the Excel files.")
    else:
        with st.expander("Excel data found for this part", expanded=True):
            st.text(evidence)

        question = st.text_input("Ask a question about this part",
                                 placeholder="What material is this part?")
        if st.button("Ask") and question.strip():
            with st.spinner("Thinking..."):
                answer = ask_llm(question.strip(), evidence)
            if answer is None:
                st.warning("The LLM is unavailable right now. The raw Excel data is shown above.")
            else:
                st.success(answer)
