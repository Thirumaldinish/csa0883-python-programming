def voting_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are allowed to vote.")
    else:
        years_left = 18 - age
        print(f"You are allowed to vote after {years_left} years.")

voting_eligibility()
