from unit import *
from sensors import *
from non_binary_unit_stat import *
from plotter import *
from data import *
from stat_hypos import *
from logger import *


class GoodControl:
    def __init__(self, uncond_sample, cond_sample, non_binary_unit):
        self.non_binary_unit = non_binary_unit
        self.uncond_sample = uncond_sample
        self.uncond_sample = cond_sample


class CandidatesFinder:
    def __init__(self, etalon, event_diameter, sensor_field_radius):
        self.binary_unit = BinaryUnit(u_radius=0, sensor_field_radius=sensor_field_radius,
                                      etalon=etalon, event_diameter=event_diameter, dx=0, dy=0)
        self.etalons = etalons_of3()
        self.p_value_thr = 0.00005

    def get_non_binary_candidates(self, radius, logger, sens_field_radius, u_radius):
        logger.add_text("binari detector description: " + str(vars(self.binary_unit)))
        x, y, pic = select_situation(self.binary_unit, self.etalons)
        X, Y = get_coords_for_radius(x, y, radius)
        fig = plot_points_on_pic_first_red(pic, [x] + X, [y] + Y)
        logger.add_fig(fig)
        print("find candidates on radius " + str(radius))
        good_controls = []
        for i in range(len(X)):
            etalon = make_measurement(pic, X[i], Y[i], sens_field_radius)
            dx = X[i] - x
            dy = Y[i] - y
            print("candidate " + str(i) + ": DX,DY=" + str(dx) + ", " + str(dy))
            non_binary_unit = NonBinaryUnit(u_radius=u_radius, sensor_field_radius=sens_field_radius, etalon=etalon,
                                            dx=dx, dy=dy)
            logger.add_text(str(vars(non_binary_unit)))

            stat_obj = NonBinaryUnitStat(non_binary_unit)
            uncond_sample = stat_obj.get_unconditional_sample(sample_size=300)
            cond_sample = stat_obj.get_conditional_sample(condition=self.binary_unit.apply, sample_size=30)
            if is_control_characterstic(uncond_sample, cond_sample, self.p_value_thr):
                gc = GoodControl(uncond_sample, cond_sample, non_binary_unit)
                good_controls.append(gc)
            logger.add_text("num cond samples = " + str(len(cond_sample)))
            visualise_two_samples(uncond_sample, cond_sample, logger)
        return good_controls

    def get_good_controls(self):
        good_controls_dict = {}
        for radius in range(1, 10):
            pass

def make_exp0():
    logger = HtmlLogger("it14_ex0")
    cf = CandidatesFinder(etalon=224, event_diameter=15, sensor_field_radius=0)
    cf.get_non_binary_candidates(radius=3, logger=logger, sens_field_radius=0, u_radius=1)
    logger.close()


if __name__ == "__main__":
    make_exp0()

