num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

act = input("min[-], max[+], med[/]: ")

if act == "-":
    result = min(num1, num2, num3)
elif act == "+":
    result = max(num1, num2, num3)
if act == "/":
    result = (num1+num2+num3)/3

print(f"Результат - {result}")
