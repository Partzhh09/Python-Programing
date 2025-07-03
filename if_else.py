marks = int(input("Enter Your marks:"))
if (marks >= 80 and marks <= 100):
    print("You got A+ grade")
elif (marks >= 70 and marks <= 80):
    print("You got A grade")
elif (marks >= 60 and marks <= 70):
    print("You got B grade")
elif (marks >= 50 and marks <= 60):
    print("You got C grade")
else:
    print("You are Failed")