print("Welcome to the tip calculator! ")
total_bill=float(input("What was the total bill? "))
tip=int(input("How much percent would you like to add? "))
guests=int(input("How many people to split the bill? "))

finalbill=round(total_bill*(1+tip/100)/guests,2)

print(f"Each person has to throw in {finalbill}€")
