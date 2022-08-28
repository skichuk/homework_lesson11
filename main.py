from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_skill, get_candidate, get_candidates_by_name

app = Flask(__name__)

FILEPATH = 'candidates.json'

candidates = load_candidates_from_json(FILEPATH)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/candidates')
def get_candidates():
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:x>')
def get_candidate(x):
    candidate = get_candidate(x, candidates)
    if candidate:
        return render_template('single.html', candidate=candidate)
    else:
        return 'NOT FOUND'


@app.route('/search/<name>')
def get_candidates_by_name(name):
    candidate_name = get_candidates_by_name(name, candidates)
    if candidate_name:
        return render_template('search.html', candidate=candidate_name)
    else:
        return "NOT FOUND"


@app.route('/skills/<skill>')
def get_skills(skill):
    candidates_by_skill = get_candidates_by_skill(skill, candidates)
    if candidates_by_skill:
        render_template('skill.html', users=candidates_by_skill)
    else:
        return "NOT FOUND"


if __name__ == '__main__':
    app.run()
