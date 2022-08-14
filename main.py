from flask import Flask
from utils import load_candidates_from_json, get_candidates_by_skill, get_candidate, get_candidates_by_name

app = Flask(__name__)

FILEPATH = 'candidates.json'

data = load_candidates_from_json(FILEPATH)


if __name__ == '__main__':
    app.run(port=5000)
