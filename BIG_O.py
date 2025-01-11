# O(n)
def printitems(n):
    for i in range(n):
        print(i)
printitems(10)

''' Here the values displayed by the forloop is depends on
the parameter 'n' values passed in the function so it
------O(n)-----'''

___________________________________________________________


def printitems(n):
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j)
printitems(10)

'''Here the values displayed by the forloop is depends on
the parameter 'n' values passed in the function, it passed
2 times, even if it is passed n time, it should be make as
O(n+n)= O(2n) here the constant value 2 should be dropped
-------O(n)---------'''

__________________________________________________________

def printitems(n):
    for i in range(n):
        for j in range(n):
         print(i,j)
printitems(10)
'''Here the values are printed from 00 to 99 so it is in order
of 2 times like n*n = n^^2, so it will be displayed as
------O(n^^2)-----'''

___________________________________________________________

def printitems(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
              print(i,j,k)
printitems(10)
'''Here the values are printed from 000 to 999, so it takes
order of 3 n*n*n = n^^3, so it will be displayed O(n^^3),
but even it has n number of orders it should follow only 2nd
order ------ O(n^^2)--------'''

__________________________________________________________

def printitems(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
printitems(10)
'''Here the first for loop gives O(n^^2) and the second for
loop gives O(n), so they would be added O(n^^2 + n) here the
dominant one will be stayed and non-dominant one will be
dropped so here O(n^^2) is dominant so O(n) will be dropped
--------O(n^^2)-----------'''

____________________________________________________________

def printitems(n):
    print(n+n*n)
printitems(10)
'''Here there is only one operation is done O(1)''''
____________________________________________________________

def printitems(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
printitems(1,2)
'''Here there are two different values are fed, like a and b
if n values passed it should have same value but here a != b
so it will be displayed seperately like ------O(a+b)-----'''

___________________________________________________________