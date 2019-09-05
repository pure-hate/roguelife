from PIL import Image
from entity_module import Entity
import pygame

class Hungry:
    def __init__(self):
        self.ccal = 1000
        self.proteins = 100
        self.fats = 100
        self.carbohydrates = 100

    def update(self, entities):
        self.ccal -= 1  # TODO: сделать голод
        # print(self.ccal)

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


class Sprite:
    def __init__(self, sprite):
        self.sprite = sprite

    def get(self):
        return self.sprite


class Inventory:
    def __init__(self, *things):
        self.__inv__ = things


class Solid:
    pass

class Playable:
    pass

class GlobalMap:
    def __init__(self, map_file):
        self.img = Image.open(map_file)
        self.height = self.img.size[1]
        self.wight = self.img.size[0]

    def loadmap(self,world):
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

