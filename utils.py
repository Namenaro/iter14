from random import choice
import random

def select_random_pic(pics):
    return choice(pics)

def select_random_xoord_on_pic(pic):
    maxX = pic.shape[1]
    maxY = pic.shape[0]
    x = random.randint(0, maxX - 1)
    y = random.randint(0, maxY - 1)
    return x,y

def apply_binary_unit_to_pic(pic, unit):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    XYs = []

    for y in range(0, ymax):
        for x in range(0, xmax):
            matches = unit.apply(pic, x, y)
            if len(matches) > 0:
                XYs.append([x,y])
    return XYs

def select_situation(binary_unit, pics):
    pic = select_random_pic(pics)
    XY = apply_binary_unit_to_pic(pic, binary_unit)
    index = random.randint(0, len(XY)-1)
    return XY[index][0], XY[index][1]
