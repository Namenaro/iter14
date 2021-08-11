from stat.basic_stat import SensRadiusesEmpiricDatabase
from unit import NonBinaryUnit
from data import *

class BinaryUnitStat:
    def __init__(self, nonbinary_unit, pics=None):
        self.nonbinary_unit=nonbinary_unit
        self.pics = pics
        if pics is None:
            self.pics = get_diverse_set_of_numbers(100)

    def get_unconditional_sample(self, sample_size=300):
        # в случайных точках случайгых картинок проводим замер этим юнитом,
        # результат (число) записываем в выборку, возвращаем ее
        pass

    def get_conditional_sample(self):
        # пробегаем по всем картинкам, в каждой точке проверяя condition
        # в тех точках, где condition=True, провоим замер этим юнитом,
        # результат (число) записываем в выборку, возвращаем ее
        pass
