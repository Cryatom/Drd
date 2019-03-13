"""print()
postavy = ["Gandalf", "Frodo"]
atributy = {"Gandalf": {"zivoty": "20", "mana": 50}}

zivoty = atributy["Gandalf"].get("zivoty")
print(zivoty)

vyber_postavy = int(input("vyber postavu: "))
if vyber_postavy == 0:
    print("Tvoje meno" + postavy[vyber_postavy])
"""
import random
from pprint import pprint


class MapObject:
    def __init__(self, name="empty", shortcut="-"):
        self.name = name
        self.shortcut = shortcut


class Entity(MapObject):
    def __init__(self, name, shortcut, vitality, stamina, strenght, level=1):
        MapObject.__init__(self, name, shortcut)
        self.name = name
        self.vitality = vitality
        self.stamina = stamina
        self.strenght = strenght
        self.level = level

    def attack(self, enemy):
        utok = random.randint(1, 21) * self.strenght
        enemy.vitality -= utok
        self.stamina -= 10
        print(f"{self.name} did {utok} dmg to {enemy.name}")

    def is_dead(self, ):
        if self.vitality <= 0:
            return True
        return False

    def level_up(self):
        self.vitality *= 1.5
        self.stamina *= 1.5
        self.strenght *= 1.5


class Hero(Entity):

    def __init__(self, name, shortcut, vitality, stamina, strenght, max_experience=1000, current_experience=0):
        Entity.__init__(self, name, shortcut, vitality, stamina, strenght)
        self.current_experience = current_experience
        self.max_experience = max_experience

    def hero_level_up(self):
        self.level_up()
        self.max_experience += 1000

    def xp(self, enemy):
        self.current_experience += enemy.experience
        if self.current_experience >= self.max_experience:
            self.level += 1
            over_limit = self.current_experience - self.max_experience
            self.current_experience = over_limit
            self.hero_level_up()


class Enemy(Entity):

    def __init__(self, name, shortcut, vitality, stamina, strenght, experience):
        Entity.__init__(self, name, shortcut, vitality, stamina, strenght)
        self.experience = experience

    def enemy_level_up(self):
        self.level_up()
        self.experience *= 1.5


class Location:

    def __init__(self, name, min_level=1, x=3, y=3, enemies=3):
        self.location_map = [[MapObject() for row in range(x)] for col in range(y)]
        self.name = name
        self.x = x
        self.y = y
        self.min_level = min_level
        self.enemies = enemies

    def map_gen(self):
        mapa = [[self.location_map[col][row].name for row in range(self.x)] for col in range(self.y)]
        for i in range(len(mapa)):
            print(*mapa[i], sep="   ")
            print("\n")

    def random_map_spot(self):
        return [random.randint(0, self.y) - 1][random.randint(0, self.x) - 1]

    def random_enemy_spawn(self):
        enemies_spawned = self.enemies
        while enemies_spawned > 0:
            enm = random.choice(enemy)
            # if type is MapObject():
            self.location_map[self.random_map_spot()] = enm
            enemies_spawned -= 1

    def random_potion_spawn(self):
        for i in range(3):
            enm = random.choice(enemy)
            # if type is MapObject():
            self.location_map[random.randint(0, self.y) - 1][random.randint(0, self.x) - 1] = enm  # prehozeny x a y
            enemies_spawned -= 1


class Potions(MapObject):
    def __init__(self, name, shortcut, experience=0, vitality_refill=0, exp_amount=1, vit_amount=1):
        MapObject.__init__(self, name, shortcut)
        self.experience = experience
        self.vitality_refill = vitality_refill
        self.exp_amount = exp_amount
        self.vit_amount = vit_amount


def fight(me, enemy):
     while True:
        me.attack(enemy)
        if enemy.is_dead():
            me.xp(enemy)
            print("Enemy died")
            break

        enemy.attack(me)
        if me.is_dead():
            print("You died")
            break


enemy = \
    [
        Enemy("orc", "e", 250, 100, 10, 200),
        Enemy("uruk", "e",  350, 100, 15, 300),
        Enemy("orc on the beast", "e", 300, 100, 18, 450),
        Enemy("uruk captain", "e", 380, 100, 20, 5,)
    ]

hero = \
    [
        Hero("Gandalf", "h", 300, 100, 30),
        Hero("Aragorn", "h", 350, 100, 25),
        Hero("Legolas", "h", 250, 100, 35),
        Hero("Gimli", "h", 400, 100, 20)
    ]

boss = \
    [
        Enemy("Nazgul", "b", 600, 200, 30, 800),
        Enemy("Ringwraith", "b",  650, 200, 35, 1600),
        Enemy("Balrog", "b",  700, 200, 40, 2400),
        Enemy("Saruman", "b",  750, 200, 45, 3200)
    ]


locations = \
    [
        Location("Shadow Forest", 1, 3, 5, 3)
    ]

potions = \
[
    Potions("Healt Potion", "hp", vitality_refill=50),
    Potions("Experience Potion", "hp", experience=200)

]

# print(hero[0].current_experience)
# print(locations[0].map)
# # print(locations[0].random_enemy_spawn(enemy[0].shortcut))
# print(locations[0].map[random.randint(0, 2)][random.randint(0, 2)])
# locations[0].random_enemy_spawn(enemy[0].shortcut)
locations[0].random_enemy_spawn()
locations[0].map_gen()



