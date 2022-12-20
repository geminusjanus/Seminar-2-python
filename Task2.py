# n = int(input('Enter number N '))
# multiplication = 0
# for i in range(n):
#     multiplication = i * n
#     print(multiplication)

n = int(input('Enter number N '))
multiplication = 1
 
for i in range(1, n+1):
    multiplication *= i
    print(multiplication, end= ' ')