stores_revenue = [[10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100, 100, 0, 2]]

def max_sum_finding(stores_revenue):
    """
    >>> max_sum_finding([[10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100, 100, 0, 2]])
    343
    """
    max_sum = sum(stores_revenue[0])
    i = 1
    number_of_stores = len(stores_revenue)
    while i < number_of_stores:
        if sum(stores_revenue[i]) > max_sum:
            max_sum = sum(stores_revenue[i])
    return max_sum


