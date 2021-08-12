from data import *
from utils import *

class CandidatesFinder:
    def __init__(self, binary_unit):
        self.binary_unit = binary_unit
        self.etalons = etalons_of3()

    def get_nearest_candidates(self):
       x, y =select_situation(self.binary_unit, self.pics)


