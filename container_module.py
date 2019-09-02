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
        print(self._entities[0].components,"ololo")
        print(self._entities[0].has("Sprite"))

        for s in self._entities:
            if s.has("Sprite") and s.has("Coordinates"):
                sprite = s.get("Sprite").get()
                screen.blit(sprites[sprite], s.get("Coordinates").get())