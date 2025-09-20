from math import *

print("Thank you for using maeth!!!")

class Constants:
    def __init__():
        print("constants are being used in here.")
    def euler_e(multiply=1):
        return e * multiply
    def py(multiply=1):
        return pi * multiply
    class ErrorConstants:
        def __init__():
            print("WARNING: ERROR CONSTANTS ARE INCLUDED")
        infinity = inf
        NotANumber = nan

class advMath:
    def squareR(num):
        return num**0.5
    def sine(num, acc=10):
        result = 0
        for n in range(acc):
            # term = (-1)^n * x^(2n+1) / (2n+1)!
            numerator = (-1)**n * (num ** (2*n + 1))
            denominator = 1
            for k in range(1, 2*n + 2):
              denominator *= k  # factorial
              result += numerator / denominator
        return result
    def factorial(num):
        if (num<0):
            print("Error: factorial can't support negative numbers")
        elif (num==0):
            return 1
        else:
            return num * factorial(num - 1)
    class advadvMath:
        def root(num, root=2):
            return num**(1/root)
        def reciprocal(num):
            return 1/num
        def tetration(base, trexponent):
            if (trexponent==0):
                return base
            else:
                return base ** advMath.advadvMath.tetration(base, trexponent-1)
    class perandarea:
        def squareper(side):
            return side*4
        def squarearea(side):
            return side**2
        def triangleper(sides):
            return sum(sides)
        class triangleareas:
            def triangleareaH(base, height):
                return (base*height)/2
            def Etrianglearea(side):
                return (advMath.squareR(3)/4).side**2
        def rectangleper(bases, heights):
            return (bases*2)+(heights*2)
        def rectanglearea(bases, heights):
            return bases*heights
        def rhombusper(side):
            return side*4
        def rhombusarea(Mdiag, mdiag):
            return Mdiag*mdiag
        def rhombiper(base, height):
            return (base*2)+(height*2)
        def rhombiarea(base, height):
            return base*height
        def trapeziumper(Mbase, mbase, side):
            return Mbase+mbase+(side*2)
        def trapeziumarea(Mbase, mbase, height):
            return (height(Mbase+mbase))/2
        def circleper(diameter):
            return Constants.py()*diameter
        def circlearea(radius):
            return Constants.py()*(radius**2)
        class shapez:
            def regularshapeper(side, amount):
                return side*amount
            def regularshapearea(apothem, side, amount):
                return (advMath.perandarea.shapez.regularshapeper(side, amount)*apothem)/2
            def irregularshapeper(sides):
                return sum(sides)
            def irregularshapearea(sides):
                return advMath.perandarea.shapez.irregularshapeper(sides)*len(sides)
            
#THE CODE BELOW IS DEPRACTED, PLEASE DO NOT ADD IT
"""
class capacitor:
    def __init__(self, info, arrayint=0):
        self.info[arrayint] = info
    def setcap(self, data, arrayint=0):
        self.info[arrayint] = data
        print("Capacitor info has changed!")
    def empty(self, arrayint=0):
        self.info[arrayint] = ""
        print("Emptied!")
    def returndata(self, arrayint=0):
        return self.info[arrayint]
"""
    
