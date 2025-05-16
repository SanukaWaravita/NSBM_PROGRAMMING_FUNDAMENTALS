def digit_reverse():
    num = int(input("Enter a number (at least 2 digits): "))
    if num < 0:
        is_negative = True
    else:
        is_negative = False
    rev_str = str(abs(num))[::-1]
    rev_int = int(rev_str)
    if is_negative:
        return -rev_int
    else:
        return rev_int

print(f"The reverse number : {digit_reverse()}")