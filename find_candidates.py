from unit import *
from sensors import *
from non_binary_unit_stat import *
from plotter import *
from data import *
from stat_hypos import *
import uuid

class Control:
    def __init__(self, uncond_sample, cond_sample, non_binary_unit):
        self.uuid=uuid.uuid4()
        self.non_binary_unit = non_binary_unit
        self.uncond_sample = uncond_sample
        self.uncond_sample = cond_sample
        self.p_val = measure_samples_difference(uncond_sample, cond_sample)
        probs1, bins = get_hist(uncond_sample, nbins=20)
        probs2, bins = get_hist(cond_sample, nbins=20)
        self.all_diff = measure_hist_difference3(probs1, probs2)
        self.max_diff = measure_max_hist_difference(probs1, probs2)


class CandidatesFinder:
    def __init__(self, etalon, event_diameter, sensor_field_radius):
        self.binary_unit = BinaryUnit(u_radius=0, sensor_field_radius=sensor_field_radius,
                                      etalon=etalon, event_diameter=event_diameter, dx=0, dy=0)
        self.etalons = etalons_of3()


    def get_non_binary_candidates(self, radius, sens_field_radius, u_radius):
        x, y, pic = select_situation(self.binary_unit, self.etalons)
        X, Y = get_coords_for_radius(x, y, radius)
        controls = []
        for i in range(len(X)):
            etalon = make_measurement(pic, X[i], Y[i], sens_field_radius)
            dx = X[i] - x
            dy = Y[i] - y
            non_binary_unit = NonBinaryUnit(u_radius=u_radius, sensor_field_radius=sens_field_radius, etalon=etalon,
                                            dx=dx, dy=dy)
            stat_obj = NonBinaryUnitStat(non_binary_unit)
            uncond_sample = stat_obj.get_unconditional_sample(sample_size=300)
            cond_sample = stat_obj.get_conditional_sample(condition=self.binary_unit.apply, sample_size=30)
            c = Control(uncond_sample, cond_sample, non_binary_unit)
            controls.append(c)
        return controls

    def get_good_controls(self):
        controls_dict = {}
        for control_radius in range(1, 10):
            controls = self.get_non_binary_candidates(control_radius, sens_field_radius=0, u_radius=0)
