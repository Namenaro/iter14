from unit import *
from sensors import *
from non_binary_unit_stat import *
from plotter import *


class CandidatesFinder:
    def __init__(self):
        self.binary_unit = BinaryUnit(u_radius=0, sensor_field_radius=0, etalon=253, event_diameter=50, dx=0,dy=0)
        self.etalons = etalons_of3()

    def get_simplest_candidates(self, radius, logger):
       x, y, pic =select_situation(self.binary_unit, self.etalons)
       X, Y = get_coords_for_radius(x, y, radius)
       print("find candidates on radius " + str(radius))
       for i in range(len(X)):
           etalon = make_measurement(pic, X[i], Y[i], 0)
           dx = X[i] - x
           dy = Y[i] - y
           print("candidate " + str(i) + ": DX,DY="+ str(dx)+", "+str(dy))
           non_binary_unit = NonBinaryUnit(u_radius=0, sensor_field_radius=1, etalon=etalon, dx=dx, dy=dy)
           logger.add_text(str(vars(non_binary_unit)))

           stat_obj = NonBinaryUnitStat(non_binary_unit)
           uncon_sample = stat_obj.get_unconditional_sample()
           cond_sample = stat_obj.get_conditional_sample(condition=self.binary_unit.apply)
           logger.add_text("num cond samples = "+ str(len(uncon_sample)))
           fig = visualise_two_samples(uncon_sample, cond_sample)
           logger.add_fig(fig)








