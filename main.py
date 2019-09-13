from entity_module import *
from container_module import *
from components import *
from update_module import *
from items import *

world = Container()

player = Entity(
    world,
    Playable(),
    Coordinates(64, 64),
    Hungry(),
    Name("Vasya"),
    Sprite("Player"),
    Health(),
    Timer(),)
player.set(Inventory(world, player, Bread(player, world), Bread(player, world), Bread(player, world)))
world.add_entity(player)
world.player = player

globalmap = Entity(
    world,
    GlobalMap("map2.png"))
world.add_entity(globalmap)
globalmap.get("GlobalMap").loadmap(world)



for i in range(1000):  # тестируем на тысяче персонажей
    player = Entity(
        world,
        Coordinates(10+(i*10), 10+i),
        Hungry(),
        Name("Vasya"),
        Sprite("Player"),
        Health())

    world.add_entity(player)

for i in range(1):  # тестируем на тысяче персонажей
    player = Entity(
        world,
        Coordinates(128, 128),
        Hungry(),
        Name("Vasya"),
        Sprite("Player"),
        Health())
    player.set(Inventory(world, player, Bread(player, world), Bread(player, world), Bread(player, world)))
    player.set(Trader(player))
    player.set(Menu(player))
    world.add_entity(player)



while True:
    update(world)

