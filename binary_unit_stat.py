from data import *
from utils import *

class BinaryUnitStat:
    def __init__(self, binary_unit, pics=None):
        self.binary_unit=binary_unit
        self.pics = pics
        if pics is None:
            self.pics = get_diverse_set_of_numbers(100)

    def get_unconditional_sample(self, sample_size=300):
        # в случайных точках случайгых картинок проводим замер этим юнитом,
        # результат (ноль или один) записываем в выборку, возвращаем ее
        activations = []
        while True:
            if len(activations) == sample_size:
                return activations
            pic = select_random_pic(self.pics)
            x, y = select_random_xoord_on_pic(pic)
            matches = self.binary_unit.apply(pic, x, y)
            if len(matches)>0:
                activation = 1
            else:
                activation = 0
            activations.append(activation)

    def get_conditional_sample(self, condition):
        # пробегаем по всем картинкам, в каждой точке проверяя condition
        # в тех точках, где condition=True, провоим замер этим юнитом,
        # результат (ноль или один) записываем в выборку, возвращаем ее
        ymax = self.pics[0].shape[0]
        xmax = self.pics[0].shape[1]
        activations = []
        for pic in self.pics:
            for y in range(0, ymax):
                for x in range(0, xmax):
                    if condition(pic, x, y):
                        matches = self.binary_unit.apply(pic, x, y)
                        if len(matches) > 0:
                            activation = 1
                        else:
                            activation = 0
                        activations.append(activation)
        return activations


