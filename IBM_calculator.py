weight = float(input("Ingresa tu peso\n"))
height = float(input("Ingresa tu altura\n"))

bmi = round(weight / (height ** 2),2)
print(f"Tu BMI es igual a :{bmi}")

if bmi < 18.5:
    print("UNDERWEIGHT")
elif bmi < 24.9:
    print("NORMAL")
else:
    print("OVERWEIGHT")