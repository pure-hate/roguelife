from entity_module import *
from container_module import *
from components import *
from update_module import *
from items import *

world = Container()
world.timer = Timer()

player = Entity(
    world,
    Playable(),
    Coordinates(64, 64),
    Hungry(),
    Name("Vasya"),
    Sprite("Player"),
    Health(),)
player.set(Inventory())
player.get("Inventory").add(Bread())
player.get("Inventory").add(Bread())
world.add_entity(player)
world.player = player

world.map = Entity(
    world,
    GlobalMap("map2.png"))

world.map.get("GlobalMap").loadmap(world)



for i in range(1000):  # тестируем на тысяче персонажей
    player = Entity(
        world,
        Coordinates(10+(i*10), 10+i),
        Hungry(),
        Name("Vasya"),
        Sprite("Player"),
        Health())

    world.add_entity(player)

for i in range(1):  # торговец
    player = Entity(
        world,
        Coordinates(128, 128),
        Hungry(),
        Name("Vasya"),
        Sprite("Player"),
        Health(),
        State())
    player.set(Inventory())
    player.get("Inventory").add(Bread())
    player.set(Trader())
    player.set(Menu())
    player.set(Path())
    world.add_entity(player)



while True:
    update(world)

