
# Day 2.3 - Life in weeks
# Date: 11/11/2022

'''

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

'''

# TODO Hacerlo en condiciones calculando con exactitud desde el día actual, considerando bisiestos, días reales de cada mes ...

'''

from datetime import date

edad = int(input("¿Cuál es tu edad actual?"))
hoy = date.today()

hoy_str = str(date.today())

año_hoy = int(hoy_str[0:4])
mes_hoy = int(hoy_str[5:7])
semana_hoy = hoy.isocalendar()[1]
dia_hoy = int(hoy_str[8:])

print(f"{año_hoy}  {mes_hoy}  {dia_hoy}, semana {semana_hoy}")

'''

edad = int(input("¿Cuál es tu edad actual?\n"))

dias = (90 - edad) * 365
semanas = (90 - edad) * 52
meses = (90 - edad) * 12

print(f"Te quedan {dias} días, {semanas} semanas y {meses} meses.")