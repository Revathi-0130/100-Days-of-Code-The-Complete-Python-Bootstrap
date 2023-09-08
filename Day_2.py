# code to split the bill amount among the number of people

print("Welcome to splitting of bill calculator")

bill_amount = float(input("What is the total bill amount?\n"))

tip_percent = int(input("What is the tip percent?\n"))

total_people = int(input("How many number of peolpe?\n"))

split_amount = (bill_amount * (1 + (tip_percent/100)))/total_people

print(round(split_amount, 2))
