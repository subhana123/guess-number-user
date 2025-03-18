import streamlit as st
import random

def main():
    st.set_page_config(page_title="Guess the Number Game (User)", page_icon="🔢")
    st.title("🔢 Guess the Number Game (User)")

    st.write("Think of a number between 1 and 100, and I'll try to guess it!")

    if 'low' not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.attempts = 0

    if st.button("Make a Guess"):
        if st.session_state.low <= st.session_state.high:
            st.session_state.attempts += 1
            guess = (st.session_state.low + st.session_state.high) // 2
            st.write(f"Is your number {guess}?")

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("📉 Too Low", key='low'):
                    st.session_state.high = guess - 1
            with col2:
                if st.button("📈 Too High", key='high'):
                    st.session_state.low = guess + 1
            with col3:
                if st.button("🎉 Correct", key='correct'):
                    st.success(f"I guessed your number {guess} in {st.session_state.attempts} attempts!")
                    st.session_state.low = 1
                    st.session_state.high = 100
                    st.session_state.attempts = 0
        else:
            st.warning("Hmm... Something went wrong. Let's start over!")
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.attempts = 0


if __name__ == "__main__":
    main()
