from app.lib import *

stores_revenue = [[1,2,3,4,5,6,7], [8,9,5,10,6], [4, 2, 11, 3, 12, 13], [10, 20, 30, 40, 50, 60, 70], [15, 100, 26, 100, 100, 2], [1, 2, 3], [1,1,1], [2,2,2,], [1, 2, 3], [100]]

print('Номер магазина с максимальной выручкой за неделю:', max_sum_store_finding(stores_revenue))
print('Номер магазина с максимальной средней выручкой за неделю:', max_average_store_finding(stores_revenue))
print('Номер магазина с максимальной выручкой за день:', max_revenue_store_finding(stores_revenue))
print('Номер магазина с минимальной выручкой за день:', min_revenue_store_finding(stores_revenue))
print('Топ 3 дневной выручки магазинов за неделю:', top_three_revenue_store_finding(stores_revenue))

