def shops():
    products_to_buy = input("Введите список товаров через запятую: ").split(',')

    shop_prices = {}
    shop_number = 1
    while True:
       shop_name = input(f"Введите название {shop_number} магазина или 'стоп' для завершения: ")
       if shop_name.lower() == 'стоп':
           break

       shop_prices[shop_name] = {}
       for product in products_to_buy:
           price = float(input(f"Введите цену товара {product} в магазине {shop_name}: "))
           shop_prices[shop_name][product] = price

       shop_number += 1

    compare_prices(products_to_buy, shop_prices)

def compare_prices(products, shop_prices):
    total_prices = {}
    for shop, prices in shop_prices.items():
        total = sum([prices[product] for product in products])
        total_prices[shop] = total
        print(f"Общая стоимость покупок в {shop}: {total: .2f}")

    cheapest_shop = min(total_prices, key=total_prices.get)
    print(f"Больше всего можно сэкономить в магазине: {cheapest_shop}")

if __name__ == "__main__":
    main()