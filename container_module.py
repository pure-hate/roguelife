import pygame
import pickle
import os, sys

# for pyinstaller
#current_path = os.path.dirname(sys.executable)
#image_path = os.path.join(current_path, 'images')

current_path = os.path.abspath(os.curdir)
image_path = os.path.join(current_path, 'images')

print(os.path.dirname(sys.executable))
print(image_path)
sprites = {"Player": pygame.image.load(os.path.join(image_path, 'player.png')),
           "Grass": pygame.image.load(os.path.join(image_path, 'grass.png')),
           "Block": pygame.image.load(os.path.join(image_path, 'block.png'))}


class Container:
    # наш игровой мир
    instance = None
    viewport = (0,0)

    def __init__(self):
        Container.instance = self
        self.player = None
        self._systems = []
        self._entities = []

    def add_system(self, system):
        self._systems.append(system)

    def add_entity(self, entity):
        self._entities.append(entity)

    def get_system(self, clazz):
        return self._systems[clazz]

    def has_system(self, clazz):
        if clazz in self._systems:
            return self.get_system(clazz)
        else:
            return None

    def get_solid(self, coords):
        for s in self._entities:
            if s.has("Coordinates") and s.has("Solid"):
                if s.get("Coordinates").get() == coords:
                    return True

    def get_entity(self, coords):
        ret = []
        for s in self._entities:
            if s.has("Coordinates"):
                if s.has("Coordinates").get() == coords:
                    ret.append(s)
                    print(ret)
        return ret

    def save(self):
        f = open(r'save.sav', 'wb')
        pickle.dump(self._entities, f)
        f.close()
        f = open(r'save2.sav', 'wb')
        pickle.dump(self._systems, f)
        f.close()

        print("Saved!")

    def load(self):
        f = open(r'save.sav', 'rb')
        self._entities = pickle.load(f)
        self.player = self._entities[0]
        f.close()
        f = open(r'save2.sav', 'rb')
        self._systems = pickle.load(f)
        f.close()

        print("Loaded!")

    def update(self):
        for s in self._systems:
            if hasattr(s, "update"):
                s.update(self._entities)

    def draw(self, screen):

        coords = self.player.get("Coordinates").get()
        viewport = ((coords[0] - 15 * 16), (coords[1] - 15 * 16))
        #print(self._entities[0])
        for s in self._entities:
            if s.has("Sprite"):
                coords = s.get("Coordinates").get()
                if coords[0] > viewport[0] and coords[1] > viewport[1]:
                    if coords[0] < viewport[0]+800 and coords[1] < viewport[1]+600:
                        sprite = s.get("Sprite").get()
                        screen.blit(sprites[sprite], (coords[0]-viewport[0], coords[1]-viewport[1]))

        coords = self.player.get("Coordinates").get()
        sprite = self.player.get("Sprite").get()
        screen.blit(sprites[sprite], (coords[0] - viewport[0], coords[1] - viewport[1]))
