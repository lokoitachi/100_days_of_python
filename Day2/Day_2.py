print("Welcome to the tip calculator.")

receipt = input("What was the total bill= $")

ask_for_tip = input("What percentage would you like to give? 10, 12, or 15? ")

ask_for_people_quantity = input("How many people to split the bill? ")

bill_without_tip = float(receipt)

convert_to_percentage = float(ask_for_tip) / 100

calculate_tip = bill_without_tip * convert_to_percentage

total_bill = bill_without_tip + calculate_tip

split_bill = total_bill / int(ask_for_people_quantity)

round_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${round_bill}")
