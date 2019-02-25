# stores_revenue = [[10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100, 100, 0, 2]]

def max_sum_store_finding(stores_revenue):
    """
    >>> max_sum_store_finding([[10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100, 100, 0, 2], [1, 2, 3]])
    [1]

    >>> max_sum_store_finding([[10, 20, 30, 40, 50, 60, 70], [10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100]])
    [0, 1]

    >>> max_sum_store_finding([[10, 20, 30, 40, 50, 60, 70]])
    [0]
    """
    max_sum = sum(stores_revenue[0])
    i = 0
    max_sum_store_number = []
    number_of_stores = len(stores_revenue)

    while i < number_of_stores:

        if sum(stores_revenue[i]) > max_sum:
            max_sum = sum(stores_revenue[i])
            max_sum_store_number.clear()
            max_sum_store_number.append(i)

        elif sum(stores_revenue[i]) == max_sum:
            max_sum_store_number.append(i)
        i += 1

    return max_sum_store_number

def max_average_store_finding(stores_revenue):
    """
    >>> max_average_store_finding([[1,1,1], [2,2,2,], [1, 2, 3]])
    [1, 2]

    >>> max_average_store_finding([[10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100]])
    [1]

    >>> max_average_store_finding([[10, 20, 30, 40, 50, 60, 70]])
    [0]
    """
    max_average = float(sum(stores_revenue[0])) / max(len(stores_revenue[0]), 1)
    i = 0
    max_average_store_number = []
    number_of_stores = len(stores_revenue)

    while i < number_of_stores:
        average = float(sum(stores_revenue[i])) / max(len(stores_revenue[i]), 1)

        if average > max_average:
            max_average = average
            max_average_store_number.clear()
            max_average_store_number.append(i)

        elif average == max_average:
            max_average_store_number.append(i)

        i += 1

    return max_average_store_number



