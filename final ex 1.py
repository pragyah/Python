""" Implement question number 2, 3, 4 and 5 from Session 1 Exercise as different functions in a single file."""


#1 Write a function that will convert Fahrenheit to Celsius in degrees.
print("Convert Fahrenheit to Celsius in degrees: ")
def fahr_to_cel(temp):
    celsius=(temp-32)*(5/9)
    return (celsius)
temperature=float(input("Enter temperature in Fahrenheit: "))
print("temperature in Fahrenheit= ",temperature, "is equal to temperature in Celsius=",fahr_to_cel(temperature)," degree")

print("--------------------------------------------------------------------------------------------------------------------")

#Write a program that takes seconds as time units and converts it to minutes and seconds.

def time2minsec(time):
    minutes = ((time // 60) % 60)
    seconds = (time % 60)
    return "{} minutes , {} seconds".format(minutes,seconds)
sec=int(input("Enter time in Seconds: "))
print(time2minsec(sec))
print("--------------------------------------------------------------------------------")

#3 :Consider a list of any arbitrary elements. Your code should print the length of the list and first and fourth element of the list.
def elem(elements):
    length=len(elements)
    first=elements[0]
    fourth=elements[3]
    return "Length of the list is {}. First element is {} and fourth is {} ".format(length,first,fourth)
lists=["apple","ball","cat","dog","egg","fish","ginger","horse","ice","jug","kitkat"]
print(elem(lists))
print("------------------------------------------------------------------------------------------------")

#4: Create a list of any arbitrary elements. Your code should show the list methods as pop, insert and remove
def li_method(element):
    element.pop(3)
    element.remove("cat")
    element.insert(0,"hello")
    return element
print(li_method(lists))
print('-----------------------------------------------------------------------------------------------------')
