from unit import *
from sensors import *
from non_binary_unit_stat import *
from plotter import *
from data import *
from stat_hypos import *

class CandidatesFinder:
    def __init__(self, etalon, event_diameter, sensor_field_radius):
        self.binary_unit = BinaryUnit(u_radius=0, sensor_field_radius=sensor_field_radius,
                                      etalon=etalon, event_diameter=event_diameter, dx=0,dy=0)
        self.etalons = etalons_of3()

    def get_simplest_candidates(self, radius, logger, sens_field_radius, u_radius):
       logger.add_text(str(vars(self.binary_unit)))
       x, y, pic =select_situation(self.binary_unit, self.etalons)
       X, Y = get_coords_for_radius(x, y, radius)
       fig = plot_points_on_pic_first_red(pic, [x]+X, [y]+Y)
       logger.add_fig(fig)
       print("find candidates on radius " + str(radius))
       for i in range(len(X)):
           etalon = make_measurement(pic, X[i], Y[i], sens_field_radius)
           dx = X[i] - x
           dy = Y[i] - y
           print("candidate " + str(i) + ": DX,DY="+ str(dx)+", "+str(dy))
           non_binary_unit = NonBinaryUnit(u_radius=u_radius, sensor_field_radius=sens_field_radius, etalon=etalon, dx=dx, dy=dy)
           logger.add_text(str(vars(non_binary_unit)))

           stat_obj = NonBinaryUnitStat(non_binary_unit)
           uncon_sample = stat_obj.get_unconditional_sample()
           cond_sample = stat_obj.get_conditional_sample(condition=self.binary_unit.apply)
           logger.add_text("num cond samples = "+ str(len(cond_sample)))
           visualise_two_samples(uncon_sample, cond_sample, logger)
           logger.add_fig(fig)








