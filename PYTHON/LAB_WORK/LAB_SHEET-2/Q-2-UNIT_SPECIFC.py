distancetraveled = float(input("Distance travelled by the car (in meters):"))
timetakenmins = float(input("Time taken for the car (in mins):"))

timetakensecs = timetakenmins * 60

avgspeed = distancetraveled / timetakensecs

print("The Average speed travelled by the car (in m/s):", round(avgspeed, 4))