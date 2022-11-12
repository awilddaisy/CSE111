from datetime import datetime
current_date_and_time=datetime.now()
weekday=current_date_and_time.weekday()

subtotal=float((input("Please enter your subtotal: ")))
tax= 0.06
disc_10= 0.10

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal* disc_10, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal-=discount 

sales_tax=round(subtotal * tax, 2)
print(f"Sales Tax Amount: {sales_tax:.2f}")
total=subtotal + sales_tax
print(f"Total: {total:.2f}")
