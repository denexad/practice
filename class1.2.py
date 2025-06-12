class Roman:
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


class IT(Roman):
    PRICE = {
        'Java': 5000,
        'Python': 4599,
        'C++': 5500
    }

    def __init__(self, name=None, last_name=None, birth_year=None, main_language=None, experience_year=None):
        super().__init__(name, last_name, birth_year)
        self.main_language = main_language
        self.experience_year = experience_year
        self._IT_id = None
        self.__salary = 0

    def generate_IT_id(self):
        self._IT_id = f"{self.name[:2].upper()}{self.birth_year}{self.last_name[:2].upper()}"
        return self._IT_id

    def calculate_salary(self):
        language = self.main_language
        if self.main_language in self.PRICE:
            self.__salary = self.PRICE[language] + \
                (self.experience_year)
        else:
            self.__salary = 0
        return self.__salary


IT_de = IT('Roman', 'Rudnik', 2007, 'Python', 3)
print(IT_de.set_name())
print(
    f"По розрахунках, ви навчаєтесь приблизно на курсі {IT_de.calculates_the_course(2025)}")
print(f"ID користувача: {IT_de.generate_IT_id()}")
print(f"Зарплата: {IT_de.calculate_salary()} USD")
