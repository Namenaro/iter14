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
        pass

    def get_conditional_sample(self):
        pass
