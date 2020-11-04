#Exercise 1
width=17
height=12.0
delimiter='.'
print("The value of first expression= ",width/2, "and the type of the expression is : ",type(width/2))
print("The value of first expression= ",width/2.0, "and the type of the expression is : ",type(width/2.0))
print("The value of first expression= ",height/3, "and the type of the expression is : ",type(height/3))
print("The value of first expression= ",1+2*5, "and the type of the expression is : ",type(1+2*5))
print("The value of first expression= ",delimiter*5, "and the type of the expression is : ",type(delimiter*5))

#Exercise 2 Write a program that will convert Fahrenheit to Celsius in degrees
print("Convert Fahrenheit to Celsius in degrees: ")
fahrenheit= float(input("Enter temperature in Fahrenheit: "))
celsius=(fahrenheit-32)*5/9
print("temperature in Fahrenheit= ",fahrenheit, "is equal to temperature in Celsius=",celsius," degree")

#Exercise 3: Write a program that takes seconds as time units and converts it to minutes and seconds
seconds=int(input("Enter time in Seconds: "))
s=(seconds % 60)
minutes= ((seconds//60) % 60)
print(seconds," seconds is equal to ",minutes, "minute and ",s,"seconds")


#Exercise 4:Consider a list of any arbitrary elements. Your code should print the length of the list and first and fourth element of the list.
fruits=["apple","banana","orange","avocado","kiwi"]
print("List of fruits= ",fruits)
print("Type of the list= ",type(fruits))
print("length of the list= ",len(fruits))
print("First element of the list is: ",fruits[0])
print("Fourth element of the list is: ",fruits[3])

#Exercise 5: Create a list of any arbitrary elements. Your code should show the list methods as pop, insert and remove
flowers=["rose","hibiscus","sunflower","marigold"]
print("list of flowers: ", flowers)
print("POP first element:",flowers.pop(0))
print("flowers after pop: ",flowers)
inserted=flowers.insert(1,"tulips")
print("after inserting element: ",flowers)
remove=flowers.remove("marigold")
print("after removing the element: ",flowers)









