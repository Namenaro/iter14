class BinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, event_diameter, dx,dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.A_min = etalon - event_diameter/2
        self.A_max = self.A_min + event_diameter
        self.dx = dx
        self.dy = dy

    def apply(self,pic, x,y): # returns 1 or 0
        pass


class NonBinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, dx, dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.etalon = etalon
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x, y): # returns float number
        pass