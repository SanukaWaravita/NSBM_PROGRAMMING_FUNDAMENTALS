# Consider the floating-point number 0.6523. Write a Python program to round it down to the nearest whole number using the math library. Then, compare the result with the output obtained by using the round() function. Explain the difference between the two outputs in terms of rounding behavior. 

import math

number = 0.6523

rounded = math.floor(number)

print(f"{number} to the nearest whole number is: {rounded}")
print(f"{number} to the nearest whole number is: {round(number, 0)}")
print("math.floor always rounds to the lower whole number, disregarding the decimal numbers")
print("round() always rounds to the nearest whole number; it rounds up or down depending on the decimal")