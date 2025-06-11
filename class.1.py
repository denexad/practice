class Denys:
    def __init__(self, name=None, last_name=None, birth_year=None):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculates_the_course(self, year: int):
        if self.birth_year == None:
            return None
        my_course = year - (self.birth_year + 16)
        return my_course

    def set_name(self):
        return [self.name, self.last_name]


name_last_name = Roman('Denys', 'Panasiyk', 2008)
list_name = name_last_name.set_name()
my_course = name_last_name.calculates_the_course(2025)
print(f'По розрахункам, ви навчаєтесь приблизно на курсі {my_course}')
print(list_name)
