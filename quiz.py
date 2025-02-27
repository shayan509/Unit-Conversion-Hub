import random

def get_quiz_questions():
    return [
        {"question": "Convert 1000 meters to kilometers.", "answer": 1.0},
        {"question": "Convert 5 kilograms to grams.", "answer": 5000.0},
        {"question": "Convert 32 Fahrenheit to Celsius.", "answer": 0.0},
        {"question": "Convert 1 mile to yards.", "answer": 1760.0},
        {"question": "Convert 1 liter to milliliters.", "answer": 1000.0},
        {"question": "Convert 2 kilometers to meters.", "answer": 2000.0},
        {"question": "Convert 10 pounds to ounces.", "answer": 160.0},
        {"question": "Convert 100 Celsius to Kelvin.", "answer": 373.15},
        {"question": "Convert 3 miles to feet.", "answer": 15840.0},
        {"question": "Convert 500 grams to kilograms.", "answer": 0.5},
        {"question": "Convert 12 inches to centimeters.", "answer": 30.48},
        {"question": "Convert 2.5 pounds to grams.", "answer": 1133.98},
        {"question": "Convert 1 acre to square feet.", "answer": 43560.0},
        {"question": "Convert 100 kilometers to miles.", "answer": 62.14},
        {"question": "Convert 50 milliliters to liters.", "answer": 0.05},
        {"question": "Convert 5 feet to meters.", "answer": 1.524},
        {"question": "Convert 1000 milligrams to grams.", "answer": 1.0},
        {"question": "Convert 7 days to hours.", "answer": 168.0},
        {"question": "Convert 24 hours to seconds.", "answer": 86400.0},
        {"question": "Convert 1 year to days (non-leap year).", "answer": 365.0}
    ]

def get_random_question(questions):
    return random.choice(questions)
