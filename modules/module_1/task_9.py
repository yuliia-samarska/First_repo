# Обчислення, яка вартість у поних гривнях та загальна вартість у копійках була витрачена на закупівлю продуктів

# Встановлюємо ціни на продукти
price_per_palianytsia = 60
price_per_glass = 2.4
price_per_coffee_pack = 14.3

# Кількість кожного продукту
num_palianytsias = int(input("Введіть кількість паляниць: "))
num_glasses = int(input("Введіть кількість стаканчиків: "))
num_coffee_packs = int(input("Введіть кількість кавових стіків: "))

# Обчислення загальної вартості
total_cost = num_palianytsias * price_per_palianytsia + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних гривень і копійок
total_hryvnia = int(total_cost)
total_kopiyok = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних гривнях: {total_hryvnia} гривень")
print(f"Загальна вартість у копійках: {total_kopiyok} копійок")
