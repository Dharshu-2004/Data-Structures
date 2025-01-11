LISTS

num1 = 11
num2 = num1
print("before Updating the num2")
print ("Location of num1 = ", id(num1))
print ("Location of num1 = ", id(num1))
num2 = 22
print("after Updating the num2")
print ("Location of num1 = ", id(num1))
print ("Location of num1 = ", id(num1))

output:
before Updating the num2
Location of num1 =  1517123142192
Location of num1 =  1517123142192
after Updating the num2
Location of num1 =  1517123142192
Location of num1 =  1517123142192

____________________________________________________________________
DICTIONARY

dict1 = {'value':11}
dict2=dict1
print("before Updating the dict2")
print ("Location of num1 = ", id(dict1))
print ("Location of num1 = ", id(dict2))
dict2['value']=22
print("before Updating the dict2")
print ("Location of num1 = ", id(dict1))
print ("Location of num1 = ", id(dict2))

output:
before Updating the dict2
Location of num1 =  2170432412416
Location of num1 =  2170432412416
before Updating the dict2
Location of num1 =  2170432412416
Location of num1 =  2170432412416