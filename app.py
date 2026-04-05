import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

def generate_study_materials(text):
    # Summary
    summary = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Summarize this text concisely for a student."},
                  {"role": "user", "content": text}]
    ).choices[0].message.content

    # Flashcards
    flashcards = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Create 5 Question: Answer flashcards from this text."},
                  {"role": "user", "content": text}]
    ).choices[0].message.content

    # Quiz
    quiz = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Create a 5-question multiple choice quiz with answers."},
                  {"role": "user", "content": text}]
    ).choices[0].message.content

    return summary, flashcards, quiz

# UI Design (Minimalist "Modern Framed" Style)
st.set_page_config(page_title="SBA Digital | Study Gen", layout="centered")
st.title("🧠 SBA Digital: Study Guide Generator")
st.markdown("---")

user_input = st.text_area("Paste your notes here:", height=250, placeholder="Enter your study material...")

if st.button("Generate Study Kit"):
    if user_input:
        with st.spinner("AI is crafting your study kit..."):
            s, f, q = generate_study_materials(user_input)
            st.subheader("📝 Summary")
            st.write(s)
            st.subheader("🧠 Flashcards")
            st.write(f)
            st.subheader("❓ Practice Quiz")
            st.write(q)
    else:
        st.warning("Please paste some text first!")

st.markdown("---")
st.caption("Built by SBA Digital for the next generation of students.")
