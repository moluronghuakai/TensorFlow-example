#!/usr/bin/python
from math import sqrt
R = 0.1

direction_unknow = 0
direction_up = 1
direction_down = 2

def choose_peak(data, max_d):
    "get peak from data"
    peak_value = [data[0]]
    peak_index = [0]
    current_dir = direction_unknow
    d0 = 0.0

    for index in range(1, len(data)):
        if current_dir == direction_unknow:
            if data[index] > data[index - 1]:
                current_dir = direction_up
            elif data[index] < data[index - 1]:
                current_dir = direction_down
            continue

        if current_dir == direction_up and data[index] < data[index - 1]:
            current_dir = direction_down
            d0 = (data[index - 1] - peak_value[len(peak_value) - 1])/ max_d
            if d0 >= R:
                peak_value.append(data[index - 1])
                peak_index .append(index - 1)
            continue

        if current_dir == direction_down and data[index] > data[index - 1]:
            current_dir = direction_up
            d0 = (peak_value[len(peak_value) - 1] - data[index - 1]) / max_d
            if d0 >= R:
                peak_value.append(data[index - 1])
                peak_index.append(index - 1)
            continue

    return (peak_value, peak_index)


def calc_slope(peak):
    "calc slope according to peak value"
    slope = []
    sl = 0.0

    for index in range(1, len(peak[0])):
        sl = (peak[0][index] - peak[0][index - 1]) / (peak[1][index] - peak[1][index - 1])
        slope.append(sl)

    return slope

def calc_mean(data,peak):
    "calc mean according to peak value"
    mean = []
    m1 = 0.0

    for i in range(1, len(peak[0])):
        for j in range(peak[1][i-1],peak[1][i]):
            ml += data[j]
        ml = ml / (peak[1][i] - peak[1][i-1])
        mean.append(ml)

    return mean


def calc_dist(slope,peak,mean):
    dist=[]
    d1=0.0
    for index in range(1, len(slope)):
        d1=sqrt((slope[index]-slope[index-1])**2+(peak[1][index] - peak[1][index - 1])**2+(mean[index]-mean[index-1])**2)
        dist.append(d1)

    return dist

"temp data, [0, 100]"
data0 = (10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0)
same = calc_dist(data0, peak, mean)
print(same)