        #1
print(" Welcome to the Bill Splitter App!")
print()

bill=float(input("Enter Total bill amount:"))
people=int(input("Enter number of people:"))
tip=int(input("Enter tip percentage (0,5,10,15,20):"))
print()


        #2
if people<=0:
    print("Enter number of people Again:")

if tip<=0 or bill<=0:
    if bill<=0:
        print("Error! in bill")
    if tip<=0:
        print("Error! in tip")
print()


        #3
tip_amt= (tip/100)*bill
final_bill = bill+tip
perperson= final_bill/ people

print("Tip Amount:₹",tip_amt)
print("Total Bill (with tip):₹",final_bill)
print("Each person should pay:₹",perperson)
print()


        #4
a=str(input("Would you like to calculate another bill? (yes/no):"))
while a=="yes":

    bill=float(input("Enter Total bill amount:"))
    people=int(input("Enter number of people:"))
    tip=int(input("Enter tip percentage (0,5,10,15,20):"))
    print()

    if people<=0:
        print("Enter number of people Again:")

    if tip<=0 or bill<=0:
         if bill<=0:
            print("Error! in bill")
         if tip<=0:
            print("Error! in tip")

    tip_amt= (tip/100)*bill
    final_bill = bill+tip
    perperson= final_bill/ people

    print("Tip Amount:₹",tip_amt)
    print("Total Bill (with tip):₹",final_bill)
    print("Each person should pay:₹",perperson)
    print()
    a=str(input("Would you like to calculate another bill? (yes/no):"))
    if a=="no":
        break

    
     







