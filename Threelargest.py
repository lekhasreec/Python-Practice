#Write a program to take three numbers and find the largest number
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
if num1>num2 and num1>num3:
    print("The Largest number is :", num1)
elif num2>num3 and num2>num1:
    print("The Largest Number is :", num2)
else:
    print("The Largest Number is :", num3)
    