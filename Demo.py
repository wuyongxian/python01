class DemoOne:
    def __init__(self):
        self.speed=0
        self.odometer=0
        self.time=0

    def say_state(self):
        print('I am going {} kph!'.format(self.speed))
    def accelerate(self):
        self.speed+=5
    def brake(self):
        self.speed-=5
    def step(self):
        self.odometer+=self.speed
        self.time+=1
    def average_speed(self):
        return self.odometer/self.time