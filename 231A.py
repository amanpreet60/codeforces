n = int(input("Enter the number of problems: "))

implementable_problems = 0

for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        implementable_problems += 1

print(implementable_problems)
