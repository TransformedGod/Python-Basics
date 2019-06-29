# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random

class Person:
    def __init__(self, name = "Orig", health = 10, damage = 5, armor = 5):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate(self, other):
        cl_damage = (self.damage - other.armor)
        return cl_damage

    def attack(self, other):
        calc_damage = self._calculate(other)
        other.health = other.health - calc_damage



class Player(Person):
    def __init__(self, name = "Any", health = 100, damage = 20, armor = 5):
        super().__init__(Person)
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

class Enemy(Person):
    def __init__(self, name = "Some", health = 100, damage = 15, armor = 10):
        super().__init__(Person)
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

player = Player('Игрок')
enemy = Enemy('Враг')

class Fight:
    while enemy.health > 0 and player.health > 0:
        if random.randrange(1, 3) % 2 == 0:
            player.attack(enemy)
        else:
            enemy.attack(player)

    print("Победил " + player.name if player.health > 0 else "Победил " + enemy.name)








