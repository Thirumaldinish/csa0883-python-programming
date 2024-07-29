
m1 = int(input("Enter the mark 1: "))
m2 = int(input("Enter the mark 2: "))
m3 = int(input("Enter the mark 3: "))
total = m1 + m2 + m3
average = total / 3
if average >= 90 and average <= 100:
    print("Average:", average)
    print("You got S grade")
elif average >= 80 and average < 90:
    print("Average:", average)
    print("You got A grade")
elif average >= 70 and average < 80:
    print("Average:", average)
    print("You got B grade")
elif average >= 60 and average < 70:
    print("Average:", average)
    print("You got C grade")
elif average >= 50 and average < 60:
    print("Average:", average)
    print("You got D grade")
elif average < 50 and average >= 0:
    print("Average:", average)
    print("You got F grade")
else:
    print("Please enter valid marks")
