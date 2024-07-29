
def simple_interest(principal, rate, time):
    return principal * (rate / 100) * time
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))
simple = simple_interest(p, r, t)
compound = compound_interest(p, r, t)
print("Simple Interest:", simple)
print("Compound Interest:", round(compound, 2))
