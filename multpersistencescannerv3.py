print("WELCOME TO MULTIPLICATIVE PERSISTENCE SCANNER \n")
print("CHOOSE YOUR RANGE")
print("---")
range1 = int(input("MINIMUM RANGE VALUE: "))
range2 = int(input("MAXIMUM RANGE VALUE: "))
print(" ")
multper = int(input("CHOOSE A MULTIPLICATIVE PERSISTENCE YOU WOULD LIKE TO SEARCH FOR: "))
print(" ")
print(" ")
print("PRESS ENTER TO START SEARCHING FOR MULTIPLICATIVE PERSISTENCE OF >=", multper, "WITHIN A RANGE OF (",range1, "AND", range2,")")
enter = input(" ")

rec = []
userrec = []

for num in range(range1,range2):
    num1 = num #store current number for later use
    print("number: ", num) #prints current number
    lst = [] #list to store multiplicative persistences
    total = 1
    while num > 0: #this loop is used to break down the number into its digits
        rem = num % 10
        num //= 10
        total *= rem
        if num == 0 and total > 9: #if the total is still greater than one digit, keep going
            lst.append(total)
            num = total
            total = 1
    lst.append(total)
    print(lst)
    print(" ")

    if len(lst) > 10:
        rec.append(num1)

    if len(lst) >= multper:
        userrec.append(num1)

if len(rec) > 0:
    print("THE NUMBERS WITH MULTIPLICATIVE PERSISTENCE GREATER THAN 10 ARE: ", lst)
    print(" ")

print("THERE ARE", len(userrec), "NUMBERS WITH MULTIPLICATIVE PERSISTENCE OF >=", multper, "WITHIN THE RANGE OF (",range1, "AND", range2,")")
if len(userrec) > 0:
    print("THOSE NUMBERS ARE: ", userrec)

exit = input(".......")
