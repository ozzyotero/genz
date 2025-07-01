import streamlit as st
from genztranslator import translate_genz_to_parent
import random

st.title("Gen Z ➡️ Parent Translator")

st.write("Enter a Gen Z phrase and get a funny parent translation!")

# Gen Z slang examples
GENZ_EXAMPLES = [
    "No cap",
    "Bet",
    "Slay",
    "Sus",
    "Bussin'",
    "It's giving",
    "Rizz",
    "Mid",
    "Fam",
    "Yeet",
    "Flex",
    "Vibe check",
    "Drip",
    "Salty",
    "Lit",
    "GOAT",
    "Stan",
    "Simp",
    "Snack",
    "Ghosted"
]

st.subheader("Need inspiration? Try one of these Gen Z phrases:")
examples = random.sample(GENZ_EXAMPLES, 3)
st.write(", ".join(f'\"{ex}\"' for ex in examples))

user_input = st.text_input("Gen Z phrase:")

if st.button("Translate"):
    if not user_input.strip():
        st.warning("Please enter a Gen Z phrase.")
    else:
        with st.spinner("Translating..."):
            try:
                translation = translate_genz_to_parent(user_input)
                st.success(translation)
            except Exception as e:
                st.error(f"Error: {e}") 