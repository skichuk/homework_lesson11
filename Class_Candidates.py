class Candidates:
    def __init__(self, id, name, picture, position, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f'{self.name}\n{self.picture}\n{self.position}\n{self.skills}'
