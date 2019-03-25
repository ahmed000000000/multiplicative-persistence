num = int(input("Enter a number: \n"))
total = 1

while num > 0:
    rem = num % 10
    num //= 10
    total *= rem
    if num == 0 and total > 9:
        print(total)
        num = total
        total = 1

print(total)

print(" ")
print("MULTIPLICATIVE PERSISTENCE CALCULATOR")
exit = int(input("exit..."))
