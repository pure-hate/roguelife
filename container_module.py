import pygame

sprites = {"Player": pygame.image.load("player.png"),
           "Grass": pygame.image.load("grass.png"),
           "Block": pygame.image.load("block.png")}


class Container:
    # наш игровой мир
    instance = None
    viewport = (0,0)

    def __init__(self):
        Container.instance = self
        self._systems = []
        self._entities = []

    def add_system(self, system):
        self._systems.append(system)

    def add_entity(self, entity):
        self._entities.append(entity)

    def update(self):
        for s in self._systems:
            if hasattr(s, "update"):
                s.update(self._entities)

    def draw(self,screen):
        for s in self._entities:
            if s.has("Playable"):
                coords = s.has("Coordinates").get()
                viewport = ((coords[0]-15*16), (coords[1]-15*16))
        for s in self._entities:
            if s.has("Sprite") and s.has("Coordinates"):
                coords = s.get("Coordinates").get()
                if coords[0]>viewport[0] and coords[1]>viewport[1]:
                    if coords[0] < viewport[0]+800 and coords[1] < viewport[1]+600:
                        sprite = s.get("Sprite").get()
                        screen.blit(sprites[sprite], (coords[0]-viewport[0], coords[1]-viewport[1]))