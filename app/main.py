from app.lib import *
#
# print(max_average_store_finding([[10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100]]))
stores_revenue = [[1,1,1], [3,2,2,], [1, 2, 3]]

    # """
    # >>> max_revenue_finding([[1,1,1], [2,2,2,], [1, 2, 3]])
    # [2]
    #
    # >>> max_revenue_finding([[10, 20, 30], [15, 100, 100]])
    # [1]
    #
    # >>> max_revenue_finding([[0], [0]])
    # [0,1]
    # """
max_revenue_stores = []
for element in stores_revenue:
    max_revenue_stores.append(max(element))
print(max_revenue_stores)
total_max_revenue = max(max_revenue_stores)
max_revenue_store = [max_revenue_stores.index(total_max_revenue)] * max_revenue_stores.count(total_max_revenue)
print(max_revenue_store)

