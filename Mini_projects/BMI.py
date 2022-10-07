name=input("What is your name?")
weight=int(input("How much do you weight?"))
height=float(input("How large you are? (m)"))

bmi= weight/ height**2

# Vytvor promennou kategorie a prirad ji hodnoy pomoci podminek
if bmi <=18.5:
    category ="undernourished"
elif bmi >18.5 and bmi <= 25:
    category="healthy weight"
elif bmi>25 and bmi<=30:
    category="little overweight"
elif bmi>30 and bmi<=40:
    category="obese"
else:
    category="severe obesity"

print(name,"your BMI is",bmi,", which is in category",category,".")

