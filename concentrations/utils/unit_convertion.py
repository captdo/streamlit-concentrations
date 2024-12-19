def strip_power_ten(quantity, power):
    if power == -3:
        return quantity * 1e-3
    if power == -6:
        return quantity * 1e-6
    return quantity


def set_power_ten(quantity, power):
    if power == -3:
        return quantity / 1e-3
    if power == -6:
        return quantity / 1e-6
    return quantity
