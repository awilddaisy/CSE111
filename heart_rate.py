"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

heart_rate = (int(input("Enter your age: ")))
max_rate = 220-heart_rate
low_percent = max_rate * 65 /100
high_percent = max_rate * 85/100
print (f"You should not excced this heart rate while exercising: {max_rate}")
print(f"When you exercise you should keep your heart rate between {low_percent:.0f} and {high_percent:.0f} beats per minute.")

