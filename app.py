import streamlit as st
import random
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.web {
    position: fixed;
    top: 0;
    right: 40px;
    height: 60px;
    border-left: 1px solid gray;
}
.spider {
    position: fixed;
    top: 55px;
    right: 25px;
    font-size: 28px;
    z-index: 999;
}
</style>
<div class="web"></div>
<div class="spider">🕷️</div>
""", unsafe_safe_allow_html=True)
st.title("🎮 Guess the number!")
st.write("I'm thinking of a number between 1 and 10.")
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.message = "YOU HAVE 3 ATTEMPTS ONLY!"
st.write(st.session_state.message)
st.write(f"Attempts: {st.session_state.attempts}/3")
guess = st.number_input(
  "Enter your guess",
  min_value=1,
  max_value=10,
  step=1
)
if st.button("Guess!"):
  if st.session_state.attempts < 3:
      st.session_state.attempts += 1
      if guess == st.session_state.secret:
        st.session_state.message = "YOU GOT IT!"
        st.balloons()
      elif abs(guess _ st.session_state.secret) == 1:
        st.session_state.message = "ALMOST THERE!"
      elif guess > st.session_state.secret:
        st.session_state.message = "Try lower."
      else:
        st.session_state.message = "Try higher."
      if guess != st.session_state.secret and st.session_state.attempts == 3:
        st.session_state.message = f"👎GAME OVER! IT WAS {st.session_state.secret}"
      st.rerun()
if st.button("Play again"):
    st.session_state.secret = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.message = "New game! YOU HAVE 3 ATTEMPTS."
    st.rerun()
