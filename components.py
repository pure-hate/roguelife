from PIL import Image
from entity_module import Entity
import items


class Timer:
    def __init__(self):
        self.hour = 12
        self.minutes = 0
        self.year = 2000
        self.month = 1
        self.day = 1

    def set_time(self, time):
        self.hour, self.minutes, self.year, self.month, self.day = time

    def get_time(self):
        return self.hour, self.minutes, self.year, self.month, self.day

    def get_min_and_hour(self):
        return self.hour, self.minutes

    def update(self, entities):
        self.minutes += 1
        if self.minutes > 59:
            self.minutes = 0
            self.hour += 1
        if self.hour > 23:
            self.hour = 0
            self.day += 1
        if self.day > 29:
            self.day = 1
            self.month += 1
        if self.month > 11:
            self.year += 1
            self.month = 1
        #print(self.get_time())


class Hungry:
    def __init__(self):
        self.ccal = 1000
        self.proteins = 100
        self.fats = 100
        self.carbohydrates = 100

    def update(self, entities):
        self.ccal -= 1  # TODO: сделать голод
        # print(self.ccal)

    def eat(self,ccal,pro,fats,carb):
        self.ccal += ccal
        self.proteins += pro
        self.fats += fats
        self.carbohydrates += carb
        print(self.ccal, self.proteins, self.fats, self.carbohydrates)


class Temperature:
    def __init__(self,temp=25):
        self.temp = temp
    def get(self):
        return self.temp


class Health:
    def __init__(self):
        self.hp = 100
        self.deseases = {}

    def update(self, entities):
        self.hp -= 1
        # print(self.hp, "HP")


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def set(self,x,y):
        self.x = x
        self.y = y

    def add(self,x,y):
        self.x += x
        self.y += y

    def update(self, entities):
        pass
        #print(self.x, self.y)


class Name:
    def __init__(self, name):
        self.name = name


class Inventory:
    def __init__(self, world, parent, *items):
        self.parent = parent
        self.world = world
        self.inventory = []
        for item in items:
            self.add(item)

    def add(self, item):
        self.inventory.append(item)

    def get(self):
        ret = []
        for num, obj in enumerate(self.inventory):
            ret.append(str(num) + obj.__class__.__name__)
        return ret
    def use(self):
        if self.inventory[0].use() == "delete":
            del self.inventory[0]


class State:
    def __init__(self, state="Idle"):
        self.state = state

    def set(self,state):
        self.state = state

    def get(self):
        return self.state


class Sprite:
    def __init__(self, sprite):
        self.sprite = sprite

    def get(self):
        return self.sprite


class Solid:
    pass


class Playable:
    pass


class Menu:
    def __init__(self, entity):
        self.entity = entity

    def show(self):
        print("Menu")
        if self.entity.has("Trader"):
            print("Торговец!")


class Trader:
    def __init__(self, parent):
        self.parent = parent
    def get_goods(self):
        print(self.parent.get("Inventory").get())
    def trade(self,other):
        pass



class GlobalMap:
    def __init__(self, map_file):
        self.img = Image.open(map_file)
        self.height = self.img.size[1]
        self.wight = self.img.size[0]

    def loadmap(self, world):
        self.map = list()
        for y in range(0, self.img.size[1]):
            for x in range(0, self.img.size[0]):
                if self.img.getpixel((x, y)) == (255, 255, 255, 255):
                    tile = Entity(
                        world,
                        Coordinates(x*32, y*32),
                        Sprite("Grass"),)
                    world.add_entity(tile)
                elif self.img.getpixel((x, y)) == (0, 0, 0, 255):
                    tile = Entity(
                        world,
                        Coordinates(x*32, y*32),
                        Sprite("Block"),
                        Solid())
                    world.add_entity(tile)

