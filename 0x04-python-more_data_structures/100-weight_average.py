#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    subtotal_weight = 0
    total_weights = 0

    for score, weight in my_list:
        subtotal_weight += score * weight
        total_weights += weight

    return subtotal_weight / total_weights
