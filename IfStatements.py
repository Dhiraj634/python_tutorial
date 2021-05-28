
# Using only If Statement

age = int(input("Enter your age : "))  # Taking Input from user
if age >= 18:  # checkiing if the user is eligible to give a vote or not
    print("You are eligible to give vote")

# Using if-else statement

age = int(input("Enter your age : "))  # Taking Input from user
if age >= 18:  # checkiing if the user is eligible to give a vote or not
    print("You are eligible to give vote")
else:
    print(f"wait for {18-age} years to give vote")

# Using if-elif-else statement

print("Provide your marks out of 100")
marks1 = int(input("Enter marks1 : "))
marks2 = int(input("Enter marks2 : "))
marks3 = int(input("Enter marks3 : "))
average = (marks1 + marks2 + marks3)/3
if(average < 35):
    print("Fail")
elif(average >= 35 and average < 50):
    print("Good")
elif(average >= 50 and average < 80):
    print("Very Good")
else:
    print("Excellent")

option = input("Do You want to see your average? (YES/NO) ")
if option == "YES":
    print(f"average = {average}")


# Ternary operator
age = int(input("Enter your age : "))
(print("eligible")) if (age >= 18) else (print(f"wait for {18-age} years"))
