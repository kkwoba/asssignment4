maths = int(input("Enter math marks: "))
phy = int(input("Enter physics marks: "))
geo= int(input("Enter geography marks: "))
chem = int(input("Enter chemistry marks: "))

# Calculate the average
average = (maths + phy + geo + chem) / 4

if 0 <= average <= 30:
    grade = "A"
elif 31 <= average <= 50:
    grade = "C"
elif 51 <= average <= 70:
    grade = "B"
elif 71 <= average <= 100:
    grade = "A"
else:
    grade = "Unrecognized marks"


print(f"Average Grade: {grade}")
