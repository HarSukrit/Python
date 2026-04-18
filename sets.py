set1={"Hello",11,55}
for x in set1:
    print(x)#Unordered Iteration
set1.add("Hi")
#Add any iterable(list/tuple/dictionary) 1 set to another using UPDATE() method
set2={"Hello",99,True}
set2.update(set1)

#Remove the values:
set1.discard(11)
set1.discard(11199999)
#Intersction/Intersection_update()
set3={"A","BB","C"}
set4={"BB","D","E"}
set_intersect=set3.intersection(set4)
set3.intersection_update(set4)
print("Result after intersection is:")
print(set_intersect)
print(set3)
#Similarly, we have difference and differnece_update()
#Symmetric difference and Symmetric difference update:
set5={"A","B","C"}
set6={"B","D","E"}
set_symm_diff=set5.symmetric_difference(set6)
print(set_symm_diff)