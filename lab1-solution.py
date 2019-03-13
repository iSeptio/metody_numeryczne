from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
#zad.1
x = linspace(56, 100)
y = 2*x**2 + 2*x + 2
plot(x, y)
show()

print("-"*20)

print('Insert your value here, and you will get factorial:')
x = int(input())
print("The factorial of " + str(x) + " is "+ str(math.factorial(x)))

print("-"*20)

def findMin(array):
    return amin(array), array.index(amin(array))

print("-"*20)

print('To what value of x you want to render a function:')
x = linspace(0,int(input()))
y = sin(x)*30000+x**3-x**2
legend(loc='upper right')
plot(x, y, 'b-', label='function y=x^3-x^2 +30000*sin(x)')
xlabel('x')
savefig('Example_how_to_save.pdf')
show()
