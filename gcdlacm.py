from math import gcd
def compute_gcd(a, b):
    return gcd(a, b)
def compute_lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("GCD:", compute_gcd(num1, num2))
print("LCM:", compute_lcm(num1, num2))
