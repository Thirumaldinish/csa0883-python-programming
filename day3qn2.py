def kilometers_to_miles(kilometers):
    """Function to convert kilometers to miles."""
    miles = kilometers * 0.621371
    return miles
kilometers = 5
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles:.6f} miles")
