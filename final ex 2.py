"""Implement question number 1, 2 and 4 from Session 2 Exercise as different functions in a single (.py) file."""

#1 choose a list of your choice and find the sum of all elements of that list. For eg: the sum of [6,9,7,5,4] is 31.
def sumlist(elem):
    sum=0
    for i in elem:
        sum=sum+i
    return sum
numlist=[1,2,4,5,6,8,9,12,15]

print("Sum of number of the list {} is {} ".format(numlist,sumlist(numlist)))
print("--------------------------------------------------------------------------------------")

#2 WaP that returns a list which contains common elements from two lists. Avoid the duplicate elements from lists.

def common(a, b):
    set1=set(a)
    set2=set(b)
    return set1.intersection(set2)
a=[2,3,1,7,8,10]
b=[7,0,2,3,1,8,11,12,9]
print("Common elements in set {} and set {} ".format(a,b))
print("is : ",list(common(a,b)))
print("-----------------------------------------------------------------------------------------")

#4 Write a code to ask inout from the user which is string and display the string along with its length
def user(str):
    count=0
    for i in str:
        count+=1
    return count
str1=str(input("Enter a String: "))
print("The length of the string {} is: {} ".format(str1,user(str1)))
print("-----------------------------------------------------------------------------------------")

