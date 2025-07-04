sub1 = int(input("Enter your marks sub1 : "))
sub2 = int(input("Enter your marks sub2 : "))
sub3 = int(input("Enter your marks sub3 : "))
sub4 = int(input("Enter your marks sub4 : "))
sub5 = int(input("Enter your marks sub5 : "))

result = sub1 + sub2 + sub3 + sub4 + sub5

print("Your Total Marks : ",result)

if (result >= 400 and result <= 500):
    print("You got A+ grade")
elif (result >= 300 and result <= 400):
    print("You got A grade")
elif (result >= 200 and result <= 300):
    print("You got B grade")
elif (result >= 100 and result <= 200):
    print("You got C grade")
else:
    print("You are Failed")