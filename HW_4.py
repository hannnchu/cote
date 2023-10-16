mlist = eval(input("Enter the measurements as a list: "))
mlist.sort()
lenm = len(mlist)
if lenm%2==0:
    median = sum(mlist[int(lenm/2)-1:int(lenm/2)+1])/2
    print("Median: ",median)
else:
    median = mlist[int(lenm/2)]/1
    print("Median: ",median)


