#unique elemnt, only one unique elemnt contan
mylist = [88,1,2,3,4,88,5,1,4,5,5,3,6,7]
tmp = []

for n in mylist:
    if n not in tmp:
        tmp.append(n)

mylist = tmp
print(mylist)



