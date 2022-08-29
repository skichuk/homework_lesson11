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


def get_candidate_by_id(x, candidates):
    """
    Функция возвращает кандидата по id
    """
    for item in candidates:
        if item.id == x:
            return item


def get_candidates_by_name(candidate_name, candidates):
    """
    Функция возвращает список кандидатов по имени
    """
    candidates_by_name = []
    for item in candidates:
        if candidate_name.title() in item.name.title():
            candidates_by_name.append(item.name)
    return candidates_by_name


def get_candidates_by_skill(skill_name, candidates):
    """
    Функция возвращает список кандидатов по навыку
    """
    names_by_skill = []
    for item in candidates:
        if skill_name.lower() in item.skills.lower():
            names_by_skill.append(item.name)
    return names_by_skill
