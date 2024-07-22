def get_ticket_price(age):
    """Function to determine the ticket price based on age."""
    if 0 <= age <= 3:
        return "The ticket is free."
    elif 4 <= age <= 12:
        return "The ticket price is Rs 10."
    elif age > 12:
        return "The ticket price is Rs 20."
    else:
        return "Invalid age entered."

# Input passenger's age
try:
    age = int(input("Enter the passenger's age: "))
    # Determine and print the ticket price
    ticket_price = get_ticket_price(age)
    print(ticket_price)
except ValueError:
    print("Please enter a valid age.")
