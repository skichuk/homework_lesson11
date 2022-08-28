import json
from Class_Candidates import Candidates


def load_candidates_from_json(path):
    """
    Функция загружает данные из файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    candidates = []
    for item in data:
        candidate = Candidates(item['id'], item['name'], item['picture'], item['position'], item['skills'])
        candidates.append(candidate)
    return candidates


def get_candidate(x, candidates):
    """
    Функция возвращает кандидата по id
    """
    for item in candidates:
        if item.id == x:
            return item


def get_candidates_by_name(name, candidates):
    """
    Функция возвращает кандидатов по имени
    """
    candidate_name = []
    for item in candidates:
        if item.name == name:
            candidate_name.append(item.name)
    return candidate_name


def get_candidates_by_skill(skill, candidates):
    """
    Функция возвращает кандидатов по навыку
    """
    skill_names = []
    for item in candidates:
        if skill.lower() in item.skills.lower():
            skill_names.append(item.name)
    return skill_names
