meters = float(input("Введіть кількість метрів: "))

act = input("Конвертування в - дюйми[1], милі[2], ярди[3]: ")

if act == "1":
    result = meters*39.3701
elif act == "2":
    result = meters*0.000621371
elif act == "3":
    result = meters*1.09361

print(f"Результат - {result}")