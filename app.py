from flask import Flask, request, redirect, url_for
import random

app = Flask(__name__)

# Load HTML templates
with open('/mnt/data/index.html', 'r') as file:
    index_html = file.read()

with open('/mnt/data/result.html', 'r') as file:
    result_html = file.read()

# Full list of questions with options and correct answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe"], "answer": "Blue Whale"},
    {"question": "In which year did World War II end?", "options": ["1945", "1939", "1955"], "answer": "1945"},
    {"question": "What is the boiling point of water?", "options": ["100°C", "90°C", "80°C"], "answer": "100°C"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Hemingway", "Fitzgerald"], "answer": "Shakespeare"},
    {"question": "What is the capital of Japan?", "options": ["Tokyo", "Beijing", "Seoul"], "answer": "Tokyo"},
    {"question": "How many continents are there?", "options": ["5", "6", "7"], "answer": "7"},
    {"question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific"], "answer": "Pacific"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Picasso", "Da Vinci"], "answer": "Da Vinci"},
    {"question": "What is the chemical symbol for gold?", "options": ["Gd", "Ag", "Au"], "answer": "Au"},
    {"question": "Which country hosted the 2016 Summer Olympics?", "options": ["Brazil", "China", "Japan"], "answer": "Brazil"},
    {"question": "What is the square root of 64?", "options": ["6", "7", "8"], "answer": "8"},
    {"question": "What is the hardest natural substance?", "options": ["Gold", "Diamond", "Iron"], "answer": "Diamond"},
    {"question": "Which planet has the most moons?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Jupiter"},
    {"question": "Who discovered penicillin?", "options": ["Fleming", "Curie", "Pasteur"], "answer": "Fleming"},
    {"question": "What is the smallest prime number?", "options": ["0", "1", "2"], "answer": "2"},
    {"question": "Who is known as the Father of Computers?", "options": ["Turing", "Babbage", "Lovelace"], "answer": "Babbage"},
    {"question": "What is the currency of Japan?", "options": ["Yuan", "Dollar", "Yen"], "answer": "Yen"},
]

@app.route('/')
def index():
    questions_html = ""
    for question in questions:
        question_block = f"<div class='question'><label>{question['question']}</label><br>"
        for option in question['options']:
            question_block += f"<input type='radio' name='{question['question']}' value='{option}' required> {option}<br>"
        question_block += "</div>"
        questions_html += question_block

    return index_html.replace("{% for question in questions %}", questions_html)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in questions:
        selected_answer = request.form.get(question['question'])
        if selected_answer == question['answer']:
            score += 1

    fact = "Did you know? The average score on this quiz is 50%!"
    result_page = result_html.replace("{{ score }}", str(score)).replace("{{ fact }}", fact)
    return result_page

if __name__ == '__main__':
    app.run(debug=True)
