#Q1
room_charge = float(input("Enter the room charge : "))
num_day = int(input("Enter the number of days : "))
food_charges = int(input("Enter the food charges : "))
ser_perc = int(input("Enter the Service charge : "))
sub_t = room_charge*num_day+food_charges
servicecharge = (sub_t)*(ser_perc)/100
print("your sub total is",sub_t)
print("your service charges are as follows",servicecharge)
print(f"your total bill is {servicecharge+sub_t}")
#Q2
sub1 = float(input("Enter the marks for the subject 1 :"))
sub2 = float(input("Enter the marks for the subject 2 :"))
sub3 = float(input("Enter the marks for the subject 3 :"))
sub4 = float(input("Enter the marks for the subject 4 :"))
total = sub1 + sub2 + sub3 + sub4
ave = total/4
GPA = ave/25
print(f"your total is {total}")
print(f"your average is {ave}")
print(f"your GPA is {GPA}")
#Q3
TD = float(input("Enter the travel distance: "))
FE = float(input("Enter the fuel efficiency: "))
FP = float(input("Enter the Fuel price: "))
HC = float(input("Enter the Highway charges: "))
FU = TD/FE
FC = FU*FP
print(f"Fuel usage is {FU}")
print(f"Fuel cost is {FC}")
print(f"Total Expenses are{FC +HC}")
#Q4
Sal = float(input("Enter the salary: "))
OTH = int(input("Enter the over time hours: "))
OTR = float(input("Enter the over time rates: "))
taxR = float(input("Enter the tax rate: "))
B = float(input("Bonus: "))
OT = OTH*OTR
GS = OT+Sal+B
tax = GS*(taxR)/100
netS = GS - tax
print(f"Gross salary {GS}")
print(f"TAXs are {tax}")
print(f"your net salary is {netS}")
#Q5
I_1 = float(input("Enter the price of the item: "))
Q1 = int(input("Enter the quantity of the item 1 :"))
I_2 = float(input("Enter the price of the item: "))
Q2 = int(input("Enter the quantity of the item 2 :"))
I_3 = float(input("Enter the price of the item: "))
Q3 = int(input("Enter the quantity of the item 3 :"))

DelC = float(input("Enter the delivery charges :"))
Discount = float(input("Enter the Discount : "))

total = (I_1*Q1+I_2*Q2+I_3*Q3)
subT = total + DelC
netT = subT*(100-Discount)/100
print(f"Your Total bills is {netT}")
#Q6
MF = float(input("Enter the monthly fee: "))
Num_M = int(input("Enter the number of months: "))
Reg = float(input("Enter Reg Fee: "))
PTC = input("IS there a personal Trainer: y or n ")
PT = 0
if PTC == "y":
    PT = float(input("Enter the PCharges : "))
else:
    pass
total = (MF+PT)*Num_M+Reg
print(f"Total bill is {total}")
#Q7
Num_M = int(input("Enter the number of Modules"))
M_Fee = float(input("Enter the module fee :"))
Lib_Fee = float(input("Enter the Lib Fee: "))
Reg_Fee = float(input("Enter the Reg Fee: "))
Total =  Num_M*M_Fee+Lib_Fee+Reg_Fee
print(f"The total fee for this sem is {Total}")
  
