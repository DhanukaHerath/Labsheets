Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Q1
print("Dhanuka Herath")
Dhanuka Herath
print("Kingswood College")
Kingswood College
#Single line Comment
"""Double Line Comment
Double Line Comment"""
'Double Line Comment\nDouble Line Comment'
#Q2
#we use comments to document things such as code explainatons, document functionalty without  affecting program execution
result= 22/7
print(f"22 divided by  is :{result}")
22 divided by  is :3.142857142857143
#Q3
#concatenation is the process of joing 2 or more strings end-to-end to form a new , single string
>>> declare_operation= "sum"
>>> declare_total = 8
>>> print(f"{declare_operation} is {declare_total}")
sum is 8
>>> #Q4
>>> length = 10
>>> width = 5
>>> print("The are of a rectangle with length "+ str(length) + "with width "+str(width) +" is "+ str(length*width))
The are of a rectangle with length 10with width 5 is 50
>>> #Q5
>>> name = input("Enter Your name: ")
Enter Your name: Dhanuka
>>> print("Hello,"+name+",welcome to NSBM ")
Hello,Dhanuka,welcome to NSBM 
>>> type(name)
<class 'str'>
>>> #Q6
>>> Birth_year = input("Enter Your Birth Year: ")
Enter Your Birth Year: 2004
>>> print(f"Your Birth Year is {Birth_year}")
Your Birth Year is 2004
>>> #Type casting is the process of converting variable type from one variables type to another variable type, for examples: converting 'int' to a 'str', 'int' to a 'str'.
>>> type(Birth_year)
<class 'str'>
>>> B_year = input("Enter Your Birth year: ")
Enter Your Birth year: 2004
>>> b_year = int(Birth_Year)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b_year = int(Birth_Year)
NameError: name 'Birth_Year' is not defined. Did you mean: 'Birth_year'?
>>> b_year = int(B_year)
>>> age  = 2025-b_year
>>> print(age)
21
