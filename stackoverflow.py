from flask import Flask, render_template, jsonify
from typing import NamedTuple
import pandas as pd
import requests
from bs4 import BeautifulSoup

first_page = 'https://stackoverflow.com/questions/tagged/android?tab=newest'
questions_in_a_week = []
last_Q_found = False
current_page = first_page
next_page = 1
while not last_Q_found:
    bs = BeautifulSoup(requests.get(current_page).text, 'html.parser')
    table1 = bs.find('div', {'id': 'questions'})
    for i in range(1, len(table1.contents)):
        temp = table1.contents[i]
        try:
            vote_temp = temp.find('span', {'class': 'vote-count-post'})
        except TypeError:
            break
        votes = int(''.join(vote_temp.find('strong')))
        time_ = temp.find('span', {'class': 'relativetime'})['title']
        title_ = temp.find('a', {'class': 'question-hyperlink'}).contents[0]
        url_ = temp.find('a', {'class': 'question-hyperlink'})['href']

        questions_in_a_week.append(
            {'title': title_, 'url': 'https://stackoverflow.com' + url_, 'votes': votes, 'time': time_})
        last_Q_found = pd.Timestamp.utcnow() - pd.to_datetime(time_, utc=True) > pd.Timedelta(7, unit='d')
        if last_Q_found:
            break
    if not last_Q_found:
        next_page += 1
        current_page = first_page + "&page=" + str(next_page) + "&pagesize=50"

top_questions = questions_in_a_week[:10]

questions_in_a_week.sort(key=lambda x: -x['votes'])
most_voted = questions_in_a_week[:10]

app = Flask(__name__, template_folder='templates',
            static_folder='static')


class Question(NamedTuple):
    title: str
    link: str
    time: str
    votes: int = 0


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/newest-questions')
def get_newest_questions():
    newest_questions = []

    for Q in top_questions:
        newest_questions.append(Question(Q['title'], Q['url'], Q['time']))

    return jsonify(newest_questions)


@app.route('/most-voted-questions')
def get_most_voted_questions():
    most_voted_questions = []
    for Q in most_voted:
        most_voted_questions.append(Question(Q['title'], Q['url'], Q['time'], Q['votes']))
    return jsonify(most_voted_questions)


@app.route('/questions')
def get_questions_count():
    return str(len(questions_in_a_week))


if __name__ == '__main__':
    app.run()
