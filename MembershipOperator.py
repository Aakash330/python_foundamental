"""
We can use membership operator to check whether
the given object present in given collection or not
in -> return True if object is present .
not in -> return True  if object is not present
"""
x = "Hello I am Akash"
print('H' in x)  # True
print('h' in x)  # True
print('d' in x)  # False
print('d' not in x)  # False

listData = ["Aaksh", "Mohan", "Rohan", "sandeep"]

print("aakash" in listData)  # False
print("mohan" in listData)  # False
