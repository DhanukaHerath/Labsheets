#Q1

n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2 :"))
print(f"number 1 {n1}")
print(f"number 2 {n2}")
print("now numbers will swap")
temp = n1
n1 = n2
n2 = temp
print(f"number 1 {n1}")
print(f"number 2 {n2}")

#Q2

n01 = int(input("Enter number 1 :"))
n02 = int(input("Enter number 2 :"))
if n01>n02:
    print("Largest number is number 1")
elif n02>n01:
    print("Largest number is number 2")
else:
    print("Both numbers are the same")

#Q3

n03 = int(input("Enter number 1 :"))

if n03>=0:
    print("number is a positve")
else:
    print("number is a negative")

#Q4

marks = int(input("Enter the marks :"))

if marks>=50:
    print("pass")
else:
    print("Fail")


#Q5
age = int(input("Enter the age: "))
if age >= 18:
    print("youy are Eligible to Vote this time")
else:
    print("You can't Vote this time")

#Q6

num4 = int(input("Enter a number: ")

if num4%2 == 0:
    print("Even")
else:
    print("Odd")

#Q7

num5 = int(input("Enter a number: ")

if num5>0:
    print("Positive")
elif num5<0:
    print("Negative")
else:
    print("Zero")
