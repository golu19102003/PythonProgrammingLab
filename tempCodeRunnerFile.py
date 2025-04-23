import sys
if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"Sum: {num1 + num2}")
except ValueError:
    print("Please enter valid numbers.")
    sys.exit(1)
