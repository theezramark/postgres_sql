class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True
        return "Engine started"

class ElectricMotor:
    def start(self):
        return "Silent start"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine          # passed in from outside

    def start(self):
        return self.engine.start()

print(Car("Golf", Engine(150)).start())        # Engine started
print(Car("ID.3", ElectricMotor()).start())    # Silent start