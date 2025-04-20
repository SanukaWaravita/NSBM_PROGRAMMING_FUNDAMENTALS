# Write a function integerPower(base, exponent) that returns the value of baseexponent For example, integerPower( 3, 4 ) = 3 * 3 * 3 * 3. 
# Assume that exponent is a positive, non-zero integer, and base is an integer. 
# Function integerPower should use for to control the calculation. 
# Do not use any math library functions.

def integerPower(base, exponent):
    
    result = 1

    for i in range(exponent):
        result *= base
     
    return(result)

print(f"{integerPower(3, 4)}")