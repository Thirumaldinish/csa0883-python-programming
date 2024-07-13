def calculate_total_balance(notes):
    denominations = [2000, 500, 200, 100]
    total_balance = 0
    for i, note_count in enumerate(notes):
        total_balance += note_count * denominations[i]
    return total_balance
print("Enter the denomination priority (e.g., 2000 500 200 100):")
priority = list(map(int, input().split()))
print("Enter the total number of notes for each denomination based on the priority:")
notes = list(map(int, input().split()))
total_balance = calculate_total_balance(notes)
print(f"The total available balance in the ATM machine is: {total_balance}")
