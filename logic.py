"""Логика проекта"""
from random import randint

import requests


class Pokemon:
    """
    Базовый Класс Покемон
    """
    pokemons = {}

    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(50, 100)
        self.power = randint(1, 5)
        Pokemon.pokemons[pokemon_trainer] = self


    def get_img(self):
        """
        Метод для получения картинки покемона через API
        """
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"


    def get_name(self):
        """
        Метод для получения имени покемона через API
        """
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"



    def info(self):
        """
        Метод класса для получения информации
        """
        return f"Имя твоего покеомона: {self.name} Здоровье твоего покемона: {self.hp} Сила покемона: {self.power}"


    def show_img(self):
        """
        Метод класса для получения картинки покемона
        """
        return self.img


    def attack(self, enemy):
        """
        Метод производит базовую атаку
        """
        if isinstance(enemy, Wizard): 
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):
    """
    Класс Наследник Волшебник
    """
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp += 5


    def info(self):
        return "У тебя покемон волшебник " + super().info()

class Fighter(Pokemon):
    """
    Класс Наследник Боец
    """
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.power += 10


    def info(self):
        return "У тебя покемон боец " + super().info()


    def attack(self, enemy):
        superpower = randint(5,15)
        self.power += superpower
        result = super().attack(enemy)
        self.power -= superpower
        return result + f"\nБоец применил супер-атаку силой:{superpower} "


if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")
    pokemon = Pokemon("username3")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(pokemon.info())
    print()
    print(fighter.attack(wizard))
   
