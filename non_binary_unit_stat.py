from data import *
from utils import *

class NonBinaryUnitStat:
    def __init__(self, nonbinary_unit, pics=None):
        self.nonbinary_unit=nonbinary_unit
        self.pics = pics
        if pics is None:
            self.pics, _ = get_diverse_set_of_numbers(100)

    def get_unconditional_sample(self, sample_size):
        # в случайных точках случайгых картинок проводим замер этим юнитом,
        # результат (число) записываем в выборку, возвращаем ее
        activations = []
        while True:
            if len(activations) == sample_size:
                return activations
            pic = select_random_pic(self.pics)
            x,y = select_random_xoord_on_pic(pic)
            activation = self.nonbinary_unit.apply(pic, x, y)
            activations.append(activation)


    def get_conditional_sample(self, condition, sample_size, pics=None):
        # пробегаем по всем картинкам, в каждой точке проверяя condition
        # в тех точках, где condition=True, провоим замер этим юнитом,
        # результат (число) записываем в выборку, возвращаем ее
        ymax = self.pics[0].shape[0]
        xmax = self.pics[0].shape[1]
        if pics is None:
            pics = self.pics
        activations = []
        for pic in pics:
            for y in range(0, ymax):
                for x in range(0, xmax):
                    if condition(pic, x, y):
                        activation = self.nonbinary_unit.apply(pic, x,y)
                        activations.append(activation)
                        if len(activations) >= sample_size:
                            return activations
        return activations


