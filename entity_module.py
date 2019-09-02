class Entity:
    # наш игровой объект
    all_entities = []

    def __init__(self, world, *components):
        self.components = {}
        self.current_world = world

        for component in components:
            self.set(component)

    def set(self, component):
        key = component.__class__.__name__
        self.components[key] = component
        self.current_world.add_system(component)

    def get(self, clazz):
        return self.components[clazz]

    def has(self, clazz):
        if clazz in self.components:
            return self.get(clazz)
        else:
            return None