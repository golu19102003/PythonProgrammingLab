import math
x1 = float(input("enter value of x1:"))
x2 = float(input("enter value of x2:"))
y1 = float(input("enter value of y1:"))
y2 = float(input("enter value of y2:"))
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("\n distance between (x1,y1) & (x2,y2) is :",distance)