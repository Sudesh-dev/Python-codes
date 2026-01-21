# Create a class Car with the following attributes: color, max_speed, acceleration, and tyre_friction.
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False

    def start_engine(self):
        self.is_engine_started=True
        
        
    def stop_engine(self):
        self.is_engine_started=False
        


def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    print(car.is_engine_started)  # As car is not yet started, it should print False
    car.start_engine()  # Starting the engine
    print(car.is_engine_started)  # As engine is on, it should print True
    car.stop_engine()  # Stopping the engine
    print(car.is_engine_started)  # As engine is off, it should print False