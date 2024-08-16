
"""
num1 = input('ENTER your Education : ')
num1 = int(num1)
num2 = input('Enter your Height : ')
num2 = int(num2)
num3 = input('Enter your Age : ')
num3 = int(num3)

if (num1 >= 14):
    if (num2 >= 5):
         if (num3 >= 18):
            if (num1 >= 14 and num2 >= 5 and num3 >= 18):
             print ("Eligible")
else:
     print ("Not Eligible") 
"""
# Write a program that asks for the user's first and last name and then prints a greeting using their full name.

"""
name1 = input('Enter your first nmae : ')
name2 = input('Enter your last name : ')

print('Hello', name1, name2) 
"""
# Write a program that asks for the user's birth year and calculates their age.

"""
birthyear = input('Dear please enter your birth year : ')
birthyear = int(birthyear)

current_year = input('Please enter your current year : ')
current_year = int(current_year)
Age = print(current_year - birthyear)
"""
# Write a program that calculates the Body Mass Index (BMI) based on the user's weight and height.
"""
weight = input('Please enter your weight : ')
weight = float(weight)
height = input('Please enter your height : ')
height = float(height)
totalheight = height*height
BMI= print (weight/totalheight)
"""
# Write a program that converts 
# a temperature from Celsius to Fahrenheit or from Fahrenheit to Celsius based on the user's choice.
"""
temp1 = input('Please enter a temperature : ')
temp1 = float(temp1)    

temp2 = float( 5/9*(temp1 -32)) 
                   
temp3 = float( (temp1 * 9/5) + 32)
choice = input('Results in Celcius or Fahrenheit : ')

if choice == 'Celcius':
    print(temp2)
else :
    print(temp3)
"""
# Write a program that asks the user for a number between 1 and 7 
# and prints the corresponding day of the week (e.g., 1 for Monday, 2 for Tuesday, etc.).
"""
number = input('Please enter a number between 1 and 7 : ')
number = int(number)
"""
# Write a program that calculates BMI based on weight and 
# height and then categorizes it into Underweight, Normal weight, Overweight, or Obesity.
"""
weight = input ('Enter the wieght : ')
weight = float(weight)
height = input ('Enter the height : ')
height = float(height)
totalheight = height * height
BMI = weight / totalheight

if BMI < 18.5:
    print('Underweight')
elif 18.5 < BMI <=24.9:
    print('Normal weight')
elif 24.9 < BMI <=39.9:
    print('Overweight')
else:
    print('Obese')
"""
