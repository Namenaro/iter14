from sensors import *

class BinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, event_diameter, dx,dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.A_min = etalon - event_diameter/2
        self.A_max = self.A_min + event_diameter
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x,y):  # retuurns list of coords of all 1-s
        expected_x = x + self.dx
        expected_y = y + self.dy
        matches = []
        for r in range(0, self.u_radius + 1):
            X, Y = get_coords_for_radius(expected_x, expected_y, r)
            for i in range(len(X)):
                mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
                if mean >= self.event_detector_min and mean <= self.event_detector_max:
                    matches.append([X[i],Y[i]])
        return matches


class NonBinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, dx, dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.etalon = etalon
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x, y): # returns float number
        X, Y = get_coords_less_or_eq_raduis(x + self.dx, y + self.dy, self.u_radius)
        nearest_mean = make_measurement(pic, X[0], Y[0], self.sensor_field_radius)
        for i in range(1, len(X)):
            mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
            if abs(mean - self.etalon) < abs(nearest_mean - self.etalon):
                nearest_mean = mean
        return nearest_mean