"""Implement question number 1, 2 and 6 from Session 3 Exercise as different functions in a single(.py) file"""

# 1. Write a program to display all prime numbers from 1 to 100

def prime(number):
    if number==1 or number==2:
        return True
    else:
        for i in range(2,number//2+1):
            if(number%i==0):
                return False
            else:
                return True
for i in range(1,101):
    if(prime(i)):
        print(i,end=",")
print("\n")
print("-----------------------------------------------------------------------------------------------------")

#2 Ask the user for a string and print out whether this string is a palindrome or not.
    #(A palindrome is a string that reads the same forwards and backwards.)


def isPalindrome(s):
    return s == s[::-1]

user1=str(input('Enter a string: '))
answer = isPalindrome(user1)

if answer:
    print("A string {} is Palindrome ".format(user1))
else:
    print("A string {} is not Palindrome ".format(user1))

print("-----------------------------------------------------------------------------------------------------")

#6. Create a dictionary that has a key value pair of letters and the number of occurrences of that letter in a string
#Given a string “pineapple”. The result should be as:
#{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
#Don’t worry about the order of occurrence of letters.

def dict(value):
    dictionary = {}
    for i in value:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary
value1=str(input('Enter a string: '))
print(dict(value1))
