tickets = int(input("введите количество билетов:"))

ages = []

for i in range(tickets):
    input_ages = int(input(f'введите возраст посетителя:'))
    ages.append(input_ages)


def age_price(n):
    if n < 18:
        return 0
    elif 18 <= n < 25:
        return 990
    else:
        return 1390


total_price = sum(map(age_price, ages))
discount_on_cost = int(total_price * 0.9)
if tickets > 3:
    print("стоимость всех билетов со скидкой ", discount_on_cost)
else:
    print("стоимость всех билетов", total_price)