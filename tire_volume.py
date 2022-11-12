import math
import datetime
now = datetime.datetime.now().date()

print()
print("Welcome to Discounted Tires!\n")
user_name=input("To get started, enter your name: ")
phone=input("Enter your phone number: ")
w=int(input("Enter the width of the tire in mm: "))
a=int(input("Enter the aspect ratio of the tire: "))
d=int(input("Enter the diameter of the wheel in inches: "))

def compute_data(w,a,d):
    return (w*a + 2540*d)*(math.pi*w**2*a) / 10000000000
print (f"The approximate volume is {compute_data(w,a,d):.2f} liters.")

stretch=input("Do you wish to purchase new tires? YES or NO: ").upper()

if stretch == 'YES':
    print("A sales associate will contact you shortly. Thank you.")
elif stretch == 'NO':
    print("Have a nice day!")

print()
print("---USER INFO---")
print(user_name)
print (now.strftime("%B %d, %Y"))
print()

with open("volumes.txt", "w") as file:
    file.write("User Info\n")
    file.write(f"{user_name}, {phone}\n")
    file.write(f"{now}\n")
    file.write(f"{w}, {a}, {d}, {compute_data(w,a,d):.2f}")
