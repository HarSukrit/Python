list1=["AB",1,True]

list2=list(("Apple","Papaya",2,5,True))

print(len(list1))
print(list1[1])
print(list1[0:2])

#Change a Range of item values: you can also change the length of list by adding more/less items
list1[0:2]=["Flowers"]
list1.insert(2,"Value")
list1.append(False)
list1.extend(list2)#extend allows to append any iterbale i.e.lists,tuple,sets,dict etc.
list1.remove("Flowers")
list1.pop(0)
list1.clear()
#Iterate over the llist:
for i in range(len(list2)):
    print(list2[i])
for x in list2:
    print(x)
list3=[5,9,2,1,10]
list3.sort()
list3.sort(reverse=True)
def myFunc(n):
    return abs(n-50)
list3.sort(key=myFunc)
list2.reverse()
#Copying list
list4=list3.copy()
list4=list(list3)
list5=list3+list4
