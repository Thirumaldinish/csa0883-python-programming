import math

def find_gcd(a, b):
    return math.gcd(a, b)

def find_lcm(a, b):
    
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd
num1 = 12
num2 = 18

gcd_result = find_gcd(num1, num2)
lcm_result = find_lcm(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_result}")
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
