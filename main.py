from entity_module import *
from container_module import *
from components import *
from update_module import *

world = Container()

player = Entity(
    world,
    Playable(),
    Coordinates(32, 32),
    Hungry(),
    Name("Vasya"),
    Sprite("Player"),
    Health())
world.add_entity(player)
world.player=player

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
# player = Entity(
#     world,
#     Coordinates(10,10),
#     Hungry(),
#     Name("Vasya"),
#     Sprite("Player"),
#     Health())
#
# world.add_entity(player)


while True:
    update(world)

