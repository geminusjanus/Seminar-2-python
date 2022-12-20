# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = float(input("Enter floating point number: "))

def sumDigits(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр = {sumDigits(num)}")

# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
# if isfloat(num) == False:
#    exit
# print(isfloat('s12'))
# print(isfloat('1.123'))