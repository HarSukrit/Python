tuple1=("Apple","Banana","Pineapple",True,11,12345)
print(len(tuple1))
tuple2=tuple(("Apple","Kiwi"))
print(tuple1[0])
print(tuple1[0:3])
if "Banana" in tuple1:
    print("Banana is present in tuple1")
#Mutating Tuples:
x=("A","b")
y=list(x)
y[1]="Kiwiw"
x=tuple(y)
print("Mutating tuple",x)

#Add tuple to tuple:
tuplex=("Apple","B")
tupley=("cherry",)
tupley+=tuplex
print(tupley)
#Multiply tuples:
tupleMul=tuplex*2
print(tupleMul)

#Delete tuple:
del tuplex

#Unpacking tuple values:
fruits=("Apple","Banana","Orange")
(green,yellow,orange)=fruits
print(green)
print(orange)
#Methods in tuple:
tuple1.count(True)
tuple1.index(True)