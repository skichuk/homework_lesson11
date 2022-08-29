from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_skill, get_candidate_by_id, get_candidates_by_name

app = Flask(__name__)

FILEPATH = 'candidates.json'

candidates = load_candidates_from_json(FILEPATH)


@app.route('/')
def page_index():
# Первое задание впихнул сюда
    return render_template('index.html')


@app.route('/candidates')
def get_candidates():
# Вывод всех кандидатов
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def get_candidate(x):
# Вывод кандидатов по id
    candidate = get_candidate_by_id(x, candidates)
    if candidate:
        return render_template('single.html', candidate=candidate)
    else:
        return 'NOT FOUND'


@app.route('/search/<candidate_name>')
def get_name(candidate_name):
# Вывод кандидатов по имени
    candidates_by_name = get_candidates_by_name(candidate_name, candidates)
    if candidates_by_name:
        return render_template('search.html', candidates=candidates_by_name)
    else:
        return "NOT FOUND"


@app.route('/skill/<skill_name>')
def get_names_by_skill(skill_name):
# Вывод кандидатов по навыку
    candidates_by_skill = get_candidates_by_skill(skill_name, candidates)
    if candidates_by_skill:
        return render_template('skill.html', skill=skill_name, users=candidates_by_skill)
    else:
        return "NOT FOUND"


if __name__ == '__main__':
    app.run()
