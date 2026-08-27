# Обчислення кількості годин, хвилин та секунд у n-й кількості секунд

n = 3600000003764

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

print(f"У {n} секундах міститься {hours} год., {minutes} хв. та {seconds} с.")
