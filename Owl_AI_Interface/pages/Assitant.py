import streamlit as st

st.title("Ask Owl AI 🤖")

with st.form("assistant_form"):
    user_name = st.text_input("Your Name")
    user_input = st.text_area("Your Question", height=150)
    submit = st.form_submit_button("Submit")

if submit:
    if user_name and user_input:
        st.success(f"Hello {user_name} 👋")

        st.markdown("### Owl AI Response")
        st.write(
            "This is a placeholder response. "
            "The system is designed to integrate real AI models "
            "for intelligent decision-making and assistance."
        )
    else:
        st.warning("Please complete all fields.")
