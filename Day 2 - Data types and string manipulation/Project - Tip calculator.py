
# Day 2 Project - Tip calculator
# Date: 12/11/2022

'''

If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

Example Input

Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7

Example Output

Each person should pay: $19.93

'''

print("¡Bienvenido al calculador de propinas!")

cuenta = float(input("¿Cuál ha sido el importe total?\n"))
propina = int(input("¿Cuánta propina quieres dejar, 10%, 12% ó 15%?\n").strip("%"))
pax = int(input("¿Entre cuantos repartís la cuenta?\n"))

total = cuenta * (1 + (propina/100))

individual = round(total/pax, 2)

print(f"Cada persona debe pagar {individual} €.")