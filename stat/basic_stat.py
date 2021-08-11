from data import *
from sensors import *

import matplotlib.pyplot as plt
import numpy as np
import json
import os.path

# Перебираем все возможные сенсорные радиусы и для каждого стороим гистограмму активаций,
# собираемую по разноообразным картинкам. В каждой гисто одни и те же границы бинов (self.bins).
# Рассчитываем вероятность того, что при заданном sensor_field_radius,
# мы, елозя взглядом в пределах u_radius, хоть раз словим активацию из [minA, maxA],
# т.е. рассчитваем вероятность события теоретически
class SensRadiusesEmpiricDatabase:
    def __init__(self):
        self.nbins = 20
        self.bins = None

    def _get_hist(self, values, min_val=0, max_val=255):
        if not isinstance(values, np.ndarray):
            values = np.array(values)
        (probs, bins, _) = plt.hist(values, bins=self.nbins,
                                    weights=np.ones_like(values) / len(values), range=(min_val, max_val))
        if self.bins is None:
            self.bins = bins
        return probs, bins

    def _get_activations_for_sens_radius(self, sens_radius, pics):
        ymax = pics[0].shape[0]
        xmax = pics[0].shape[1]
        means = []
        for pic in pics:
            for centery in range(0, ymax):
                for centerx in range(0, xmax):
                    val = get_sensory_array(pic, centerx, centery, sens_radius)
                    means.append(np.mean(val))
        return means

    def _count_hist_for_sens_radius(self, sens_radius, pics):
        values = self._get_activations_for_sens_radius(sens_radius, pics)
        probs, bins = self._get_hist(np.array(values))
        return probs, bins

    def _count_hists_for_sens_radiuses(self):
        sens_radiuses = range(0, 14)
        npics = 100
        pics, _ = get_diverse_set_of_numbers(npics)
        stat_data = {}
        for sens_radius in sens_radiuses:
            print("get stat for raduis " + str(sens_radius))
            probs, bins = self._count_hist_for_sens_radius(sens_radius, pics)
            stat_data[sens_radius] = {'probs': probs.tolist(), 'bins': bins.tolist()}
        return stat_data


    def _get_hists_for_sensradiuses(self):
        filename = "../sens_radiuses_hists.json"
        if os.path.isfile(filename):
            with open(filename) as f:
                data = json.load(f)
                return data
        print("gather simple sensory stat...")
        data = self._count_hists_for_sens_radiuses()
        with open(filename, 'w') as f:
            json.dump(data, f)
        return data

    def get_hist_for_sens_radius(self, sens_radius):
        return self._get_hists_for_sensradiuses()[sens_radius]

    def get_binary_event_distr(self, minA, maxA, sensor_field_radius, u_radius):
        # Рассчитываем вероятность того, что при заданном sensor_field_radius,
        # мы, елозя взглядом в пределах u_radius, хоть раз словим активацию из [minA, maxA]
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        probs, bins = self.get_hist_for_sens_radius(sensor_field_radius)

        # найдем какие бины надо "слить" друг с другом, чтоб получить вероятность события А
        start_bin = None
        end_bin = None
        for j in range(len(bins) - 1):
            if minA >= bins[j] and minA <= bins[j + 1]:
                start_bin = j
            if maxA >= bins[j] and maxA <= bins[j + 1]:
                end_bin = j

        # считаем вероятность события А без учета неопределенности по управлению
        A_probability = 0
        for j in range(start_bin, end_bin + 1):
            A_probability += probs[j]

        # теперь учтем, что управлений множество, и надо чтоб "хотя бы одно" привело к А
        not_A_probability = 1 - A_probability
        size_u_field = get_size_of_field_by_its_radius(u_radius)
        p_of_not_even_one_in_u_set = not_A_probability ** size_u_field  # вер-ть, что для всех u выполнится !А
        p_of_at_least_one_in_u_set = 1 - p_of_not_even_one_in_u_set  # вер-ть, что хотя бы для одного u выполнится А
        return [p_of_at_least_one_in_u_set, p_of_not_even_one_in_u_set]

if __name__ == "__main__":
    database = SensRadiusesEmpiricDatabase()
    print(database.get_hist_for_sens_radius(4))