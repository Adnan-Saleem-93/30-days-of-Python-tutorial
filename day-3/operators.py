# Exercises - Day 3

# Declare your age as integer variable
my_age = 32
# Declare your height as a float variable
my_height = 5.11
# Declare a variable that store a complex number
complex = 1j+2
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input('Enter base: ')
height = input('Enter height: ')
area = 0.5 * int(base) * int(height)
print("area of triangle = ", area)
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')

perimeter = int(side_a) + int(side_b) + int(side_c)
print('perimeter of triangle = ', perimeter)


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area =  length * width
print("area of triangle = ", area)
perimeter = 2 * (length + width)
print('perimeter of triangle = ', perimeter)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Enter radius: '))
PI = 3.14
area =  PI * radius ** 2
print("area of circle = ", area)
circumference = 2 * PI * radius
print("circumference of circle = ", circumference)
# Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# For the equation y = 2x - 2 (which is in the form y = mx + b):
# Slope (m) = 2
# Y-intercept (b) = -2 (where the line crosses the y-axis)
# X-intercept: set y = 0, solve for x: 0 = 2x - 2, so x = 1

slope = 2
y_intercept = -2
y = 0
# equation becomes:
# 2 * x = 2
# dividing by 2 both sides
# (2/2) * x = 2/2
x_intercept = 1

print(f"Equation: y = 2x - 2")
print(f"Slope: {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
isEqual = int(float("9.8")) == 10
assertion  = 'not equal' if isEqual == False else "equal"
print(f'9.8 is {assertion} to 10')
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Pay of th person = ", pay)
