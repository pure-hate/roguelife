from PIL import Image
from entity_module import Entity
import datetime

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
        print(self.get_time())


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

    def set(self, x, y):
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
    def __init__(self):
        self.inventory = []

    def add(self, item):
        item.parent = self.parent
        item.world = self.world
        self.inventory.append(item)

    def get(self):
        ret = []
        for num, obj in enumerate(self.inventory):
            ret.append(str(num) + obj.__class__.__name__)
        return ret

    def use(self):
        print("Use")
        if self.inventory[0].use() == "delete":
            del self.inventory[0]


class State:
    def __init__(self, state="Idle"):
        self.state = state

    def set(self, state):
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
    def __init__(self):
        pass

    def show(self):
        print("Menu")
        if self.parent.has("Trader"):
            print("Торговец!")


class Trader:
    def __init__(self):
        pass
    def get_goods(self):
        print(self.parent.get("Inventory").get())

    def update(self, entities):
        if self.world.timer.hour == 19:
            self.parent.has("State").set("ToHome")
        if self.parent.has("State").get() == "ToWork":

            if self.parent.has("Path").path:
                self.parent.get("Path").step_path()
            else:
                #self.parent.get("Path").path = self.parent.has("Path").find_path((64, 64))
                self.parent.has("State").set("Work")

        elif self.parent.has("State").get() == "ToHome":
            if self.parent.has("Path").path:
                self.parent.get("Path").step_path()
            else:
                #self.parent.get("Path").path = self.parent.has("Path").find_path((128, 1280))
                self.parent.has("State").set("Idle")



    def trade(self,other):
        pass



class GlobalMap:
    def __init__(self, map_file):
        self.img = Image.open(map_file)
        self.height = self.img.size[1]
        self.wight = self.img.size[0]

    def load_map_pathfind(self):
        map = list()
        li = ""
        for y in range(0, self.img.size[1]):
            for x in range(0, self.img.size[0]):
                if self.img.getpixel((x, y)) == (255, 255, 255, 255):
                    li += " "
                elif self.img.getpixel((x, y)) == (0, 0, 0, 255):
                    li += "#"
            map.append(li)
            li = ""
        return map

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


class Path:
    def __init__(self):
        self.path = []
        self.img = Image.open("map2.png")
        self.height = self.img.size[1]
        self.wight = self.img.size[0]

    def load_map_pathfind(self):
        map = list()
        li = ""
        for y in range(0, self.img.size[1]):
            for x in range(0, self.img.size[0]):
                if self.img.getpixel((x, y)) == (255, 255, 255, 255):
                    li += " "
                elif self.img.getpixel((x, y)) == (0, 0, 0, 255):
                    li += "#"
            map.append(li)
            li = ""
        return map

    def step_path(self):
        if self.path:
            # если еще не дошли до точки
            self.parent.has("Coordinates").set(self.path[0][1]*32, self.path[0][0]*32)
            del self.path[0]

    def find_path(self, end):
        print("Ololo")
        starttime = datetime.datetime.now()
        worldmap = self.load_map_pathfind()
        print("Karta ",datetime.datetime.now() - starttime)
        start = self.parent.get("Coordinates").get()[0]//32, self.parent.get("Coordinates").get()[1]//32
        end = end[0]//32, end[1]//32
        print(start)
        print(end)
        path = []
        map_temp = []

        for i in worldmap:
            temp = [a for a in i]
            for n, i in enumerate(temp):
                if i == " ":
                    temp[n] = 10000
                if i == "#":
                    temp[n] = 99999
            map_temp.append(temp)

        if map_temp[start[1]][start[0]] == 10000:
            map_temp[start[1]][start[0]] = 0

        path_temp = [(n, x.index(0)) for n, x in enumerate(map_temp) if 0 in x]
        if map_temp[path_temp[0][0] + 1][path_temp[0][1]] == 10000: map_temp[path_temp[0][0] + 1][path_temp[0][1]] = 1
        if map_temp[path_temp[0][0]][path_temp[0][1] + 1] == 10000: map_temp[path_temp[0][0]][path_temp[0][1] + 1] = 1
        if map_temp[path_temp[0][0]][path_temp[0][1] - 1] == 10000: map_temp[path_temp[0][0]][path_temp[0][1] - 1] = 1
        if map_temp[path_temp[0][0] - 1][path_temp[0][1]] == 10000: map_temp[path_temp[0][0] - 1][path_temp[0][1]] = 1

        counter = 1
        while end not in path_temp and path_temp != []:

            for index1, item in enumerate(map_temp):
                for index2, item2 in enumerate(item):
                    if item2 == counter:
                        temp = (index1, index2)
                        path_temp.append(temp)

            counter += 1
            for i in path_temp:
                if map_temp[i[0] + 1][i[1]] == 10000: map_temp[i[0] + 1][i[1]] = counter
                if map_temp[i[0]][i[1] + 1] == 10000: map_temp[i[0]][i[1] + 1] = counter
                if map_temp[i[0]][i[1] - 1] == 10000: map_temp[i[0]][i[1] - 1] = counter
                if map_temp[i[0] - 1][i[1]] == 10000: map_temp[i[0] - 1][i[1]] = counter

        steps = map_temp[end[0]][end[1]]
        path.append(end)
        map_temp[end[0]][end[1]] = 100
        i = 0
        current_point = end
        while steps != 0:
            poisk = {(current_point[0] + 1, current_point[1]): map_temp[current_point[0] + 1][current_point[1]],
                     (current_point[0], current_point[1] - 1): map_temp[current_point[0]][current_point[1] - 1],
                     (current_point[0], current_point[1] + 1): map_temp[current_point[0]][current_point[1] + 1],
                     (current_point[0] - 1, current_point[1]): map_temp[current_point[0] - 1][current_point[1]]}

            for k, v in poisk.items():
                if map_temp[k[0]][k[1]] == steps - 1:
                    current_point = k
                    path.append(k)
                    steps -= 1

        path.reverse()
        print("Path ", datetime.datetime.now() - starttime)
        return path
