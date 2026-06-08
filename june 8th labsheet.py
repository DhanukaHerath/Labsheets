#Question 1

print("Welcome Vote Eligibility")
age = int(input("Enter the age: "))
if age >=18:
    citizen = input("Are you a citizen of this country, 'y' or 'n': ")
    if citizen=='y':
        print("Eligible to vote")
    else:
        print("not eligible to vote")
else:
    print("not eligible to vote")

#Question 2

print("Welcome to ATM")
pin = input("Enter the pin: ")
if pin == '1234':
    amount = int(input("Enter the amount to withdraw: "))
    if amount<=20000:
        print(f"You have withdrew {amount}")
    else:
        print("sorry insufficient amount")
else:
    print("Wrong pin")

#Question 3
print("Welcome to Scolarship program")
S_marks = float(input("Enter the student marks: "))
if S_marks>=75:
    F_income = int(input("Enter the family's financial statuts :"))
    if F_income <=50000:
        print("Eligible for the Scholarship")
    else:
        print("you are rich enought to pay for your work")
else:
    print("Not enought marks")

#Question 4

print("welcome to the Examination")
registered = input("Are you registered? 'y' or 'n' : ")
if registered ==  'y':
    paid = input("Have you paid the Examination fee,'y' or 'n' : ")
    if registered == 'y':
        print("you can access online examination")
    else:
        print("you can't access online examination")
else:
    print("you can't access online examination")

#Question 5
print("welcome to loan taker")
salary = int(input("Enter the amount of Salary: "))
if salary>=50000:
    credit = int(input("Enter the credit score: "))
    if score>= 700:
        print("Qualifies for the loan")
    else:
        print("Not qualifies for the loan")
else:
    print("Not qualifies for the loan")

#Question 6
print("Welcome to online shopping")
log = input("User logged in? 'yes' or 'no' : ")
if log == 'yes':
    cashV = int(input("Enter the amount of Item value: "))
    if cashV >=1000:
        pay = input("payemnt successful 'yes'/'no': ")
        if pay=='yes':
            print("Payment is successful")
        else:
            print("aborted")
    else:
        print("Payment is unsuccessful")
else:
    print("Payment is unsuccessful")

#Question 7
print("booking hotel room")
room = input("Rooms are available 'yes' or 'no' : ")
if room == 'yes':
    input("Enter customer ID: ")
    cus = input("Customer input ID (yes/no) : ")
    if cus == 'yes':
        adv = input("customer paid advance payment? (yes/no) : ")
        if adv == 'yes':
            stay = int(input("number of days customer statys: "))
            if stay >=1:
                print("you have booked a room")
            else:
                print("Sorry you can't book a room ")
        else:
            print("Sorry you can't book a room ")
    else:
        print("Sorry you can't book a room ")
else:
    print("Sorry you can't book a room ")
