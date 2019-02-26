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


def max_revenue_store_finding(stores_revenue):
    """
    >>> max_revenue_store_finding([[1,1,1], [2,2,2,], [1, 2, 3]])
    [2]

    >>> max_revenue_store_finding([[10, 20, 30], [15, 100, 100]])
    [1]

    >>> max_revenue_store_finding([[0], [0]])
    [0, 1]
    """
    max_revenue_stores = []
    for element in stores_revenue:
        max_revenue_stores.append(max(element))
    # print(max_revenue_stores)
    # total_max_revenue = max(max_revenue_stores)
    # max_revenue_store = [max_revenue_stores.index(total_max_revenue)] * max_revenue_stores.count(total_max_revenue)
    # print(max_revenue_store)

    len_max_revenue_stores = len(max_revenue_stores)
    total_max_revenue = max_revenue_stores[0]
    total_max_store_number = []
    number = 0
    while number < len_max_revenue_stores:
        if total_max_revenue < max_revenue_stores[number]:
            total_max_revenue = max_revenue_stores[number]
            total_max_store_number.clear()
            total_max_store_number.append(number)

        elif total_max_revenue == max_revenue_stores[number]:
            total_max_store_number.append(number)
        number += 1
    # print(total_max_store_number)
    return total_max_store_number

def min_revenue_store_finding(stores_revenue):
    """
    >>> min_revenue_store_finding([[1,1,1], [2,2,2,], [4, 2, 3]])
    [0]

    >>> min_revenue_store_finding([[10, 20, 30], [15, 100, 100]])
    [0]

    >>> min_revenue_store_finding([[0], [0]])
    [0, 1]
    """
    min_revenue_stores = []
    for element in stores_revenue:
        min_revenue_stores.append(min(element))
    # print(max_revenue_stores)
    # total_max_revenue = max(max_revenue_stores)
    # max_revenue_store = [max_revenue_stores.index(total_max_revenue)] * max_revenue_stores.count(total_max_revenue)
    # print(max_revenue_store)

    len_min_revenue_stores = len(min_revenue_stores)
    total_min_revenue = min_revenue_stores[0]
    total_min_store_number = []
    number = 0
    while number < len_min_revenue_stores:
        if total_min_revenue > min_revenue_stores[number]:
            total_min_revenue = min_revenue_stores[number]
            total_min_store_number.clear()
            total_min_store_number.append(number)

        elif total_min_revenue == min_revenue_stores[number]:
            total_min_store_number.append(number)
        number += 1
    # print(total_max_store_number)
    return total_min_store_number

def top_three_revenue_store_finding(stores_revenue):
    """
    >>> top_three_revenue_store_finding([[1,2,3,4,5,6,7], [8,9,5,10,6], [4, 2, 11, 3, 12, 13]])
    [[5, 6, 7], [8, 9, 10], [11, 12, 13]]

    >>> top_three_revenue_store_finding([[6,7], [8,9,5,10,6], [4, 2, 11, 3, 12, 13]])
    [[6, 7], [8, 9, 10], [11, 12, 13]]
    """
    top_three_revenue_store = []
    for element in stores_revenue:
        # element = list(set(element)) #если необходимо выводить только уникальные значения
        element.sort()
        top_three_revenue_store.append(element[-3:])
    return top_three_revenue_store




