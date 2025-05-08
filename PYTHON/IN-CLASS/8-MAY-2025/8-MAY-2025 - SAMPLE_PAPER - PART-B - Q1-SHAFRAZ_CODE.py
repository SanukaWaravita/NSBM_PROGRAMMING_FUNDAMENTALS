p, n, z, i = 0, 0, 0, 1

while (i<=10):
    no = int(input("Enter a number"))
    if (no > 0):
        p = p + 1
    elif (no < 0):
        n = n + 1
    else:
        z = z + 1
    
    i = i + 1

print(f"No. of positives {p}")
print(f"No. of negatives {n}")
print(f"No. of zeros {z}")