import streamlit as st
import random

# Title and Sections
st.title("Generative AI - Math Challenges")

# Select Task
task = st.sidebar.selectbox("Select a Task", ["Math Riddle Factory", "Math Meme Repair", "Creative Math Solver"])

# Math Riddle Factory
if task == "Math Riddle Factory":
    st.header("Math Riddle Factory")

    # Collect Riddles
    st.subheader("Enter 30 Math Riddles and Solutions")
    riddle_data = []
    for i in range(30):
        riddle = st.text_input(f"Riddle {i + 1}", key=f"riddle_{i}")
        solution = st.text_input(f"Solution {i + 1}", key=f"solution_{i}")
        if riddle and solution:
            riddle_data.append((riddle, solution))

    if st.button("Generate Riddles"):
        if len(riddle_data) == 30:
            st.success("Generated Riddles:")
            for _ in range(5):
                random_riddle = random.choice(riddle_data)
                st.write(f"Riddle: {random_riddle[0]} | Solution: {random_riddle[1]}")

# Math Meme Repair
elif task == "Math Meme Repair":
    st.header("Math Meme Repair")

    # Collect Incorrect Memes
    st.subheader("Enter 20 Incorrect Math Memes")
    meme_data = []
    for i in range(20):
        wrong_meme = st.text_input(f"Incorrect Meme {i + 1}", key=f"wrong_meme_{i}")
        correct_explanation = st.text_input(f"Correct Explanation {i + 1}", key=f"correct_explanation_{i}")
        if wrong_meme and correct_explanation:
            meme_data.append((wrong_meme, correct_explanation))

    meme_input = st.text_area("Enter an incorrect math meme to fix:")
    if st.button("Fix Meme"):
        if meme_input and meme_data:
            for wrong, correct in meme_data:
                if meme_input.strip() == wrong.strip():
                    st.success("Fixed Meme:")
                    st.write(correct)
                    break
            else:
                st.error("No matching meme found.")

# Creative Math Problem Solver
elif task == "Creative Math Solver":
    st.header("Creative Math Problem Solver")

    # Collect Emoji Problems
    st.subheader("Enter 30 Emoji Math Problems and Solutions")
    emoji_data = []
    for i in range(30):
        emoji_problem = st.text_input(f"Emoji Problem {i + 1}", key=f"emoji_problem_{i}")
        emoji_solution = st.text_input(f"Emoji Solution {i + 1}", key=f"emoji_solution_{i}")
        if emoji_problem and emoji_solution:
            emoji_data.append((emoji_problem, emoji_solution))

    emoji_input = st.text_area("Enter an emoji math problem to solve:")
    if st.button("Solve Emoji Math"):
        if emoji_input and emoji_data:
            for problem, solution in emoji_data:
                if emoji_input.strip() == problem.strip():
                    st.success("Solution:")
                    st.write(solution)
                    break
            else:
                st.error("No matching emoji math problem found.")

st.sidebar.info("Submit in .ipynb or .py format by March 14, 2025")
