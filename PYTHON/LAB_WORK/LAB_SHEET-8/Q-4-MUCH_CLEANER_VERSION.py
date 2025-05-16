# Function to convert Fahrenheit to Celsius
def celsius(f):
    return round((f - 32) * 5 / 9)

# Function to convert Celsius to Fahrenheit
def fahrenheit(c):
    return round((c * 9 / 5) + 32)

# Print header
print(f"{'Celsius':>8} {'Fahrenheit':>12}    ||    {'Fahrenheit':>12} {'Celsius':>8}")
print("-" * 50)

# Determine range to cover all values
celsius_range = range(0, 101)         # 0 to 100
fahrenheit_range = range(32, 213)     # 32 to 212

# Use max length of the ranges
max_length = max(len(celsius_range), len(fahrenheit_range))

# Print values in a single table row-wise
for i in range(max_length):
    # Left side: Celsius to Fahrenheit
    if i < len(celsius_range):
        c = celsius_range[i]
        f = fahrenheit(c)
        left = f"{c:>8} {f:>12}"
    else:
        left = " " * 21

    # Right side: Fahrenheit to Celsius
    if i < len(fahrenheit_range):
        f2 = fahrenheit_range[i]
        c2 = celsius(f2)
        right = f"{f2:>12} {c2:>8}"
    else:
        right = ""

    print(f"{left}    ||    {right}")
