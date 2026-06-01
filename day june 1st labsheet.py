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
