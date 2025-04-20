# Write a function that takes the time as three integer arguments (for hours, minutes, and seconds) and returns the number of seconds since the last time the clock “struck 12.” 
# Use this function to calculate the amount of time in seconds between two times, both of which are within one 12-hour cycle of the clock.

def noOfSeconds(hours, minutes, seconds):
    hoursToSeconds = hours * 3600
    minutesToSeconds = minutes * 60
    totalSeconds = hoursToSeconds + minutesToSeconds
    return(totalSeconds)

print("Enter the first time below: ")
hours1 = int(input("Enter an integer value for hours: "))
minutes1 = int(input("Enter an integer value for minutes: "))
seconds1 = int(input("Enter an integer value for seconds: "))

print("Enter the second time below: ")
hours2 = int(input("Enter an integer value for hours: "))
minutes2 = int(input("Enter an integer value for minutes: "))
seconds2 = int(input("Enter an integer value for seconds: "))

time1 = noOfSeconds(hours1, minutes1, seconds1)
time2 = noOfSeconds(hours2, minutes2, seconds2)

difference = time2 - time1
if difference < 0:
    difference = -difference

print(f"\nTime difference between the two times in seconds is: {difference}")