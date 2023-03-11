# importing vlc module
# printing media
# I have written the comment  using """ to ignore the string because python is not support multi comment
"""
In this File only I have written simple
python code to understand if  and else condition
and data type  .
note :- Python have 33 reserved
following are data type in python (14)
Int,Float,Complex,Bool,Str,Bytes,ByteArray
Range,List,Tuple,Set,Frozenset,Dict,None

"""

# How to represent Int data type

"""
Decimal form -0 to 9
Binary -> prefix with 0b and 0B only accept 0, 1
octal form -> Prefix with 0o 
hex form -> 0X 
"""
a = 10
print("Decimal Form ", a)
# binary form
a = 0b10
print("Binary form ", a)

# Octal form
a = 0o10
print("octal form ", a)

#  Hex Form
a = 0X10
print("Hex form ", a)

# float data type
"""
Float data type 
f = 1.23
 we also write python value using
 exponential 
"""
f = 12.2
print(type(f))
f = 1.2e3
print("Exponential value ", f)

# Complex data type
"""
Complex Data type represent -> a+bj
"""

complexNum1 = 7 + 9.5j
complexNum2 = 8 + 1.5j

print("add of two complex number ", complexNum1 + complexNum2)
print("Real number {} and Imaginary number {} ".format(complexNum1.real, complexNum1.imag))

# bool Data type

"""
bool data type represent True and False
Internally it used 1 -> True and 0->False
"""

b = True
print("value of b ", b)
print("value of b ", b + b)  # ans 2

# str Data type
"""
String data type 
we can  write the string with
(1) single quote -> 'Akash'
(2) double quote -> "Akash"
(3) triple Quote -> 
Slicing -> slice means a piece

"""

print('single Akash')
print("double Akash")
print("""triple Akash """)

# slicing string example
sliceStr = "Akash"
print("value of 0 index is {} and value of -1 index is {}".format(sliceStr[0], sliceStr[-1]))
sliceStr = sliceStr * 5
print("After multiply the String ", sliceStr)

print("After multiply the String ", sliceStr[:8])

# check if condition
check = 10.0
if check is int:
    print("this is type int ")
else:
    print("this is not type int")

# change the into complex number
print(complex(True, False))
# change into string

print(str(10.7))

# byte Data type
"""
Byte data type represent the group of byte number just like an array
x=[10,20,30,40,50]
x=byte(x) //we need to implicit change into byte otherwise it will become list type
byte array range is 0 to 256
if once creates the bytes data type value we can not change the value
otherwise you will get type error.
"""
byteType = [10, 20, 30, 40]
byteType =bytes(byteType)
print("byte data type \n")
for i in byteType:
    print(i)

# byteArray data  type
"""
byteArray is same as byte data except this
is allow you modified the elemne
x=[10,20,30,40,50]
x=byteArray(x)
range 0 to 256
"""
x = [10, 20, 30, 40, 50, 60]
x = bytearray(x)
print("byteArray data type before modify 1 index postion:")
for i in x:
    print(i)
print('after change the value of byte array ')
x[1] = 100
for i in x:
    print(i)
print("ByteArrat ended here")

#List data type
"""
insertion order preseved
duplicate allow value is allowed
haterogeneous data type allowed
it is mutable in nature
listData=[1,9.5,"Aakash"]
"""
listData=[1,9.5,"Aakash"]
for i in listData:
    print(i)

#Tuple data type
"""
tuple data type is same as list data type
only following difference
tuple is immutable data type
tuple represented with () parenthesis
note -> Tuple is  the read only version of list
"""

t=(10,20,30)
print("Data type is {} ".format(type(t)))
for i in t:
    print(i)


#Range data type

"""
range Data type represents a sequence of number 
it is also immutable data type
r= range(10)
r =range(10,20) we can also generate between
r =range(10,20,2) we can also generate number between the gap
"""
r=range(10)
print("data type ", type(r))
for i in  r:
    print(i)

print("number between 10 to 20 with gap 3")
r=range(10,20,3)
for i in r:
    print(i)

#set Data type
"""
Insertion order is not preserved
Duplicate value is not allowed 
Hetrogenuous object are allowed
Index concept is not applicable
it mutable data type
it is represent with curly braces {}
"""
setdataType={10,20,30,30,10,"akash"}
print("data type ", type(setdataType))
print("value of setDat type ", setdataType)

#frozenset Data type
"""
it is exactly same as set except that is immutable
hence we can not perform any operation
represent the frozenset Data type
froz={10,20,30,40}
froz=frozenset(froz)
"""
froznset={10,20,30,40,"aakash"}
froznset=frozenset(froznset)
print("data type is ", type(froznset))
print("frozenset data is ",froznset)

#dict data type in android
"""
if we want to represent group of value with key value pair then go with dict type
duplicate data are nit allowed 
it is mutable data type
insertion order is not preserved
"""

dictData={"name":"Akash",102:"rahul",90:"mohan",12:"sandeep"}
print("data type is ",type(dictData))
print("value of dic type is  ",dictData)

#None data type
"""
None mens nothing or No value assosited .Like java null
"""

def m1():
    a=10

print(m1())











