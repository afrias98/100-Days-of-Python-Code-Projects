print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = 1 + float(input("What percentage tip would you like to give? 10%, 12%, 15% "))/ 100
people = int(input("How many people are splitting the bill? "))
print(f'Split evenly, each person should pay ${round((bill/people) * tip,2)}')