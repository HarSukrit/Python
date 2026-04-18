dict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":1961
}
print(dict1.keys())
#Pop
dict1.pop("model")
print("Printing dictionary after pop:",dict1)
#Pop Item:Removes last inserted key-value,note only inserted not updated.
dict1.popitem()
print("Printing dictionary after pop_item",dict1)