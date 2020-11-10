    #1. Write a program to display all prime numbers from 1 to 100
    num=1
    while(num<=100):
        count=0
        i=2
        while(i<=num//2):
            if(num%i==0):
                count=count+1
                break
            i=i+1
        if(count==0 and num!= 1):
            print(num)
        num=num+1
    #2 Ask the user for a string and print out whether this string is a palindrome or not.
    #(A palindrome is a string that reads the same forwards and backwards.)
    strg=input("Enter a String: ")
    strg=str(strg)
    reverse=strg[: : -1]
    print("Reverse of the string",strg, "is: ", reverse)
    if(strg==reverse):
        print('the String is Palindrome')
    else:
        print('Not a Palindrome String ')

    """---------------------------------------------------------------------------"""
    user=int(input("Input a number: "))
    temp=user
    rev=0
    while(user>0):
        n=user%10
        rev=rev*10+n
        user=user//10
    if(temp==rev):
        print("The number is Palindrome")
    else:
        print("Not a Palindrome")

    #3 Given a string, count all lower case, upper case, digits and special symbols.
    user1=str(input("Enter a string: "))
    upper,lower,digit,special=0,0,0,0
    for i in user1:
        if(i.count(' ')):
            continue
        else:
            if(i.isupper()):
                upper+=1
            if(i.isnumeric()):
                digit+=1
            if(i.islower()):
                lower+=1
            else:
                special+=1

    print("The given String is: ",user1)
    print("Total Uppercase: ",upper)
    print("Total Lowercase: ",lower)
    print("Total Special: ",special)
    print("Total digit: ",digit)


    #4 Write a program to display the n terms of harmonic series and their sum.
    #1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n
    numb=int(input("Input the number of terms: "))
    result=0
    for i in range(1,numb+1):
        if(i<numb):
            print(f"1/{i}", end=" + ")
            result+=1/i

        if(i==numb):
            print(f"1/{i}")
            result += 1 / i

    print("The sum of series upto {} terms: {}".format(numb,result))

    #5 Write a program to display the following pattern. Check also with different number of rows
    """   *
        **
       ***
      ****
     ***** """

    row=int(input("Enter no. of rows: "))
    k=2*row-2
    for i in range(0,row):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

#6. Create a dictionary that has a key value pair of letters and the number of occurrences of that letter in a string
#Given a string “pineapple”. The result should be as:
#{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
#Don’t worry about the order of occurrence of letters.

str1=input("ENter a String")
dictionary={}
for i in str1:
       if i in dictionary.keys():
           dictionary[i] += 1
       else:
           dictionary[i]=1
print(dictionary)

