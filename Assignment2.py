#1 choose a list of your choice and find the sum of all elements of that list. For eg: the sum of [6,9,7,5,4] is 31.
sum=0;
num=[4,5,7,2,9]
for n in range(0,len(num)):
    sum=sum+num[n]
  #  print(sum)
print("Sum of ",num,"is: ",sum)

#another way:
sum=0
num=[4,5,7,2,9]
for n in num:
    sum=sum+n
print("Sum of ",num,"is: ",sum)

#2 WaP that returns a list which contains common elements form two lists. Avoid the duplicate elements from lists.
a=[2,3,1,7,8,10]
b=[7,0,2,3,1,8,11,12,9]
set_a=set(a)
set_b=set(b)
print(set_a)
print(set_b)
common=set_a.intersection(set_b)
print("Common elements in set are: ",common)
print("Common elements in List: ",list(common))


#3 Suppose you have a list [1,2,7,12,15]
# Print each number using loop. Also print the square of each number using loop.
l=[1,2,7,12,15]
for n in range(0,len(l)):
    print("Numbers in list are: ",l[n])

for n in range(0, len(l)):
    print("Squares of numbers are: ",l[n]**2)

#4 Write a code to ask inout from the user which is string and display the string along with its length
user=str(input("Enter a String: "))
print("The String inputted by user is: ",user)
print(type(user))
length=0
for i in user:
    length=length+1
print("Length of the string is: ",length)

#5 Write a code to ask an input from the user which is a string and convert it to uppercase and lowercase
user=str(input("Enter a String: "))
print("The String inputted by user is: ",user)
print(type(user))
upper=user.upper()
lower=user.lower()
print("Uppercase: ",upper)
print("Lowercase: ",lower)




