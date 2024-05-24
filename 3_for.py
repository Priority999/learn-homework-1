"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main(count_sales):
    count = 0
    for score in count_sales:
        count += score
    return count


for summary_sale in phone:
    sum_sale = main(summary_sale['items_sold'])
    print(f'Суммарное количество продаж для "{summary_sale["product"]}": {sum_sale} раз')

total_sales_all_products = 0
total_items_all_products = 0

for summary_sale in phone:
    sum_sale = main(summary_sale['items_sold'])
    avg_sale = sum_sale / len(summary_sale['items_sold'])
    print(f'Среднее количество продаж для "{summary_sale["product"]}": {avg_sale:.2f}')
    total_sales_all_products += sum_sale
    total_items_all_products += len(summary_sale['items_sold'])


avg_sales_all_products = total_sales_all_products / total_items_all_products

print(f'\nСуммарное количество продаж всех товаров: {total_sales_all_products}')
print(f'Среднее количество продаж всех товаров: {avg_sales_all_products:.2f}')
    
# if __name__ == "__main__":
#     main()
