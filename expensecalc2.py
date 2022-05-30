#exp = [12,18,10,19,23,10]
#print("before", exp)
#print("Total items in the exp list is",len(exp))
#exp.append(25)
#print("after", exp)


exp = []
stopped = False


while not stopped:
    e = int(input("what is the expense  (type 0 to stop)  "))
    if e !=0:
          exp.append(e)
    else:
        stopped = True
print(exp)
print("total expenses:  ", sum(exp))
print("max expense: ", max(exp))