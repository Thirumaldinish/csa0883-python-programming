def calculate_simple_interest(principal, years, senior_citizen):
    if principal <= 0 or years <= 0:
        return "Invalid input. Principal and years must be positive numbers."

    rate_of_interest = 12 if senior_citizen.lower() == 'y' else 10
    interest = (principal * rate_of_interest * years) / 100
    return int(interest)

def main():
    principal = float(input("Enter the principal amount: "))
    years = int(input("Enter the no of years: "))
    senior_citizen = input("Is customer senior citizen (y/n): ")

    interest = calculate_simple_interest(principal, years, senior_citizen)

    if isinstance(interest, int):
        print("Interest:", interest)
    else:
        print(interest)

if __name__ == "__main__":
    main()
