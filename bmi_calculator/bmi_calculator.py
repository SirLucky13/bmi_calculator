# YOU CAN FIND A BMI CHART HERE!!!
# JUST HOVER OVER WITH MOUSE, HIT CTRL + CLICK FROM MOUSE
# https://en.wikipedia.org/wiki/Body_mass_index


name = input("Enter Name? ")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
if bmi < 25:
    print(name)
    print("Right On Track")
else:
    print(name)
    print("Needs Improvement")
