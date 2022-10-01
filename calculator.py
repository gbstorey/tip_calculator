print("Welcome to the tip calculator.")
total=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
numpeople=float(input("How many people to split the bill? "))
perperson = round((total*(1+tip))/numpeople,2)
print(f"Each person should pay ${perperson}")