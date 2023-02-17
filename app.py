import flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

JOBS = [
    {"id": 1, "title": "Software Engineer", "company": "Google", "location": "Mountain View", "salary": 250000},


    {"id": 2, "title": "Data Engineer", "company": "Facebook","location": "San Francisco", "salary": 200000},
    {"id": 3, "title": "Data Scientist", "company": "Microsoft","location": "Seattle", "salary": 105000},

    {"id": 4, "title": "Quantitative analyst", "Company": "Vanguard","location": "New York", "salary": 250000},
]

@app.route('/')

def index():
    return render_template('index.html', jobs=JOBS)



if __name__ == '__main__':
    app.run(debug=True)
    