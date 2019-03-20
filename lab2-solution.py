from cs50 import get_int
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#zad1

x = get_int("x: ")
y = get_int("y: ")

def calculatePerimeter(radius):
    return 2*3.14*radius

def calculateField(radius):
    return 3.14*radius**2

#zad2

print(calculateField(x),calculatePerimeter(x))
print("-"*20)
print(calculateField(y),calculatePerimeter(y))
print("-"*20)

def checkIfEven(x,y):
    if ((x%2 and y%2) == 0) and x%y==0:
        print("this numbers are even and divisible: " +str(x) +" "+ str(y))
    else:
        print("this numvers are not divisible and even")


print(checkIfEven(x,y))


#zad3

print("-"*20)

checkDivisibility = x%y == 0

checkDivisibilityLog = "x is divisible by y" if checkDivisibility else "X is not divisible by Y"
print(checkDivisibilityLog)

#zad4

print("-"*20)

def formatAndRound(x,y,decimals):
    return format(round(x/y,decimals), ".2f")

#zad5

print("-"*20)

given_number = get_int("Give number: ")
x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**2*np.exp(-0.1*R)*given_number
ax = Axes3D(plt.figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()

print(formatAndRound(x,y,10))


#0 Use alternative way of reading inputs - using library (0.5p)
#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)