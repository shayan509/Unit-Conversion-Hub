import streamlit as st
from conversions import convert_length, convert_weight, convert_temperature
from quiz import get_quiz_questions
import random

def main():
    st.title("Unit Converter")
    st.write("### Developer: Muhammad Shayan Imran")

    app_mode = st.sidebar.selectbox("Choose the app mode", ["Converter", "Quiz"])
    
    if app_mode == "Converter":
        run_converter()
    elif app_mode == "Quiz":
        run_quiz()

def run_converter():
    conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])
    value = st.number_input("Enter value to convert", min_value=0.0, format="%.2f")

    if conversion_type == "Length":
        handle_length_conversion(value)
    elif conversion_type == "Weight":
        handle_weight_conversion(value)
    elif conversion_type == "Temperature":
        handle_temperature_conversion(value)

def handle_length_conversion(value):
    from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches", "nautical miles", "light years"])
    to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches", "nautical miles", "light years"])
    result = convert_length(value, from_unit, to_unit)
    st.success(f"🎉 Converted value = **{result:.2f}** {to_unit}")

def handle_weight_conversion(value):
    from_unit = st.selectbox("From", ["kilograms", "grams", "pounds", "ounces", "newtons", "stones", "carats"])
    to_unit = st.selectbox("To", ["kilograms", "grams", "pounds", "ounces", "newtons", "stones", "carats"])
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"🎉 Converted value = **{result:.2f}** {to_unit}")

def handle_temperature_conversion(value):
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin", "Rankine"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin", "Rankine"])
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f" Converted value = **{result:.2f}** {to_unit}")

def run_quiz():
    st.header("Unit Conversion Quiz")
    questions = get_quiz_questions()

    if 'current_question' not in st.session_state:
        st.session_state.current_question = random.choice(questions)
        st.session_state.feedback = ""
        st.session_state.show_next = False
        st.session_state.question_index = 0

    st.write(st.session_state.current_question["question"])
    user_answer = st.number_input("Your answer", format="%.2f", key=f"quiz_answer_{st.session_state.question_index}")

    if st.button("Submit"):
        if abs(user_answer - st.session_state.current_question["answer"]) < 0.01:
            st.session_state.feedback = "Correct! 🎉"
        else:
            st.session_state.feedback = f"Incorrect. The correct answer is {st.session_state.current_question['answer']}."
        st.session_state.show_next = True

    st.write(st.session_state.feedback)

    if st.session_state.show_next:
        if st.button("Next Question"):
            st.session_state.current_question = random.choice(questions)
            st.session_state.feedback = ""
            st.session_state.show_next = False
            st.session_state.question_index += 1  # Increment the index to change the key

if __name__ == "__main__":
    main()
