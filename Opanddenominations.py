#bitwise operators
bitstring = "1A0B0C1"
result = int(bitstring[0])
for i in range(1, len(bitstring) - 1, 2):
    operator = bitstring[i]
    next_bit = int(bitstring[i + 1])

    if operator == 'A':   
        result &= next_bit
    elif operator == 'B': 
        result |= next_bit
    elif operator == 'C': 
        result ^= next_bit
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

