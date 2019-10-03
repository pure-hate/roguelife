class Bread:
    def __init__(self):
        self.weight = 0.1

    def use(self):
        self.parent.has("Hungry").eat(100,10,5,50)
        #self.parent.get["Hungry"].eat(100,10,5,50)
        print(self.parent.__class__.__name__, "Съел хлеб")
        return "delete"