import numpy as np

class Lander():
    def __init__(self, start_pos: tuple, planet: dict):
        self.landed = False
        self.planet = planet
        assert "radius" in planet.keys()
        assert "g" in planet.keys()
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.h = self.dist_to_surface()
        self.x_v = 0
        self.y_v = -planet["g"]
        self.x_rot = 0
        self.z_rot = 0
        self.fuel = 100
    def dist_to_surface(self):
        return np.sqrt(self.x**2+self.y**2) - self.planet["radius"]
    def step(self, main: int, x: int, z: int, x_rot: int, z_rot: int):
        # x/z axis
        self.x_v += x
        # rotation
        self.x_rot += x_rot % 360
        self.z_rot += z_rot % 360
        # height
        self.h = self.dist_to_surface()
        self.y = np.round(self.y + self.y_v,1)
        self.x = np.round(self.x + self.x_v,1)
        # engine uses
        if self.h <= 0:
            self.landed = True
        self.y_v -= self.planet["g"] + main * np.cos(np.deg2rad((-self.z_rot-90)%360))
        self.x_v -= main * np.cos(np.deg2rad(self.z_rot-90))
        # fuel
        self.fuel = np.max([0, self.fuel-main-x-z-x_rot-z_rot])