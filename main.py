# Python weight converter

weight = float(input("Enter Your weight : "))
unit = input("Kilograms or Pounds ? K or L : ")
if unit != "K" and unit !=  "k" and unit !=  "l" and unit !=  "L" :
    print(f'{unit} is not valid')
else : 
    if unit == "k" or unit == "K":
        weight = weight * 2.205
        unit = "Lbs."
    elif unit == "l" or unit == "L":
        weight = weight / 2.205
        unit = "kg"
    print(f"Your weight is : {round(weight,1)} {unit}")

