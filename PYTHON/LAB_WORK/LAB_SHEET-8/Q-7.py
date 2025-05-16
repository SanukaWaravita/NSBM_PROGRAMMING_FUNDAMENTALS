def qualityPoints():
    avg_marks = int(input("Enter the student's average mark here: "))
    if 100 <= avg_marks <=90:
        points = 4
    elif 89 <= avg_marks <= 80:
        points = 3
    elif 79 <= avg_marks <=70:
        points = 2
    elif 69 <= avg_marks <=60:
        points = 1
    else:
        points = 0
    return(points)

print(f"The student's quality point is {qualityPoints()}")