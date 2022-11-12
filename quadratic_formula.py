from math import sqrt

def compute_data(a,b,c):
    return (0-b + sqrt(b**2 - (4*a*c))) /(2*a)
        
print(compute_data(22,66,9))