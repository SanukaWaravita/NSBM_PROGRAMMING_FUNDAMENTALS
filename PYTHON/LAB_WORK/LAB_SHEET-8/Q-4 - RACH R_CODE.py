def celsius(fahrenheit):
    celsius = (fahrenheit - 32)*(5/9)
    return celsius

def fahrenheit(celsius):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

for f,c in zip(range (32,213), range (0,101)):
    print(f"{f} F = {celsius(f):.2f} C   //  {c} C = {fahrenheit(c):.2f} F")
    


