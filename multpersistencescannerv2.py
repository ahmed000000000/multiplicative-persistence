for num in range(1,10000):
    num1 = num
    print("number: ", num)
    lst = []
    total = 1
    while num > 0:
        rem = num % 10
        num //= 10
        total *= rem
        if num == 0 and total > 9:
            lst.append(total)
            num = total
            total = 1
    lst.append(total)
    print(lst)
    print(" ")

    if len(lst) > 5:
        print("HIGHEST MULTIPLICATIVE PERSISTENCE IS", num1 )
        print(num1, "HAS A MULTIPLICATIVE PERSISTENCE OF", len(lst))
        break


exit = input(".......")
