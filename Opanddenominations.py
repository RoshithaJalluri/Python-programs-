#bitwise operators
# Define the input bitstring
bitstring = "1A0B0C1"

# Start with the first bit
result = int(bitstring[0])

# Loop through the string to apply operations
for i in range(1, len(bitstring) - 1, 2):
    operator = bitstring[i]
    next_bit = int(bitstring[i + 1])

    if operator == 'A':   # AND operation
        result &= next_bit
    elif operator == 'B': # OR operation
        result |= next_bit
    elif operator == 'C': # XOR operation
        result ^= next_bit

# Print the final result
print("Result:", result)

#denomination
amount = int(input("Enter amount: "))

five_hundred_notes = amount // 500
amount %= 500
print("Five Hundred (500):", five_hundred_notes)

hundred_notes = amount // 100
amount %= 100
print("Hundred (100):", hundred_notes)

fifty_notes = amount // 50
amount %= 50
print("Fifty (50):", fifty_notes)

ten_notes = amount // 10
amount %= 10
print("Ten (10):", ten_notes)

print("Remaining amount:", amount)
