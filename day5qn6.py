
def decimal_to_binary(n):
    binary = 0
    j = 1
    while n != 0:
        i = n % 2
        binary += i * j
        n = n // 2
        j *= 10
    return binary
n = int(input("Enter the decimal number: "))
binary = decimal_to_binary(n)
print("Binary:", binary)
