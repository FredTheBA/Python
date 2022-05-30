#exp1 = input("what is the expense? ")
#exp2 = input("what is the expense? ")
#exp3 = input("what is the expense? ")
#exp4 = input("what is the expense? ")

exp = -1
total = 0

while exp !=0:
    exp = int(input("what is the expense?  (type 0 to stop)  "))
    total = total + exp
print("Your total expenditure is "  +  str(total))
