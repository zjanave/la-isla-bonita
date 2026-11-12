from main import FPS

class timer():
    def __init__(self):
        self.dt = 0
        self.dt = self.clock.tick(FPS)

    def update(self):
        self.dt = self.clock.tick(FPS)
        print(self.dt)
