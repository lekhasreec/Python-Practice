#Write a program to print all even numbers from 1 to N.
a=int(input("Enter a number:"))
for i in range(0,a+1):
    if i%2==0:
        print(i)
        