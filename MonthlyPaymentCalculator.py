print("Let's calculate your mothly percentage rate and your minimum payment!")

#User input
amount_owed = float(input("Amount owed: $"))
APR = float(input("APR: "))


#Calculations
monthly_percentage = APR /12
minimum_payment = (float(monthly_percentage) * int(amount_owed)) / 100


#output
print(f"Monthly percentage rate: {round(monthly_percentage, 3)}")
print(f"Minimum payment: ${round(minimum_payment, 2)}")
