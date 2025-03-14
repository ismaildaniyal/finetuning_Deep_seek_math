import streamlit as st
import random

# Title and Sections
st.title("Generative AI - Math Challenges")

# Select Task
task = st.sidebar.selectbox("Select a Task", ["Math Riddle Factory", "Math Meme Repair", "Creative Math Solver"])

# Math Riddle Factory
if task == "Math Riddle Factory":
    st.header("Math Riddle Factory")

    # Collect Single Riddle
    riddle = st.text_input("Enter a Math Riddle")
    solution = st.text_input("Enter the Solution")

    if st.button("Generate Riddle"):
        if riddle and solution:
            st.success("Generated Riddle:")
            st.write(f"Riddle: {riddle} | Solution: {solution}")

# Math Meme Repair
elif task == "Math Meme Repair":
    st.header("Math Meme Repair")

    # Collect Single Incorrect Meme
    wrong_meme = st.text_input("Enter an Incorrect Math Meme")
    correct_explanation = st.text_input("Enter the Correct Explanation")

    meme_input = st.text_area("Enter an incorrect math meme to fix:")
    if st.button("Fix Meme"):
        if meme_input and wrong_meme and correct_explanation:
            if meme_input.strip() == wrong_meme.strip():
                st.success("Fixed Meme:")
                st.write(correct_explanation)
            else:
                st.error("No matching meme found.")

# Creative Math Problem Solver
elif task == "Creative Math Solver":
    st.header("Creative Math Problem Solver")

    # Collect Single Emoji Problem
    emoji_problem = st.text_input("Enter an Emoji Math Problem")
    emoji_solution = st.text_input("Enter the Solution")

    emoji_input = st.text_area("Enter an emoji math problem to solve:")
    if st.button("Solve Emoji Math"):
        if emoji_input and emoji_problem and emoji_solution:
            if emoji_input.strip() == emoji_problem.strip():
                st.success("Solution:")
                st.write(emoji_solution)
            else:
                st.error("No matching emoji math problem found.")
