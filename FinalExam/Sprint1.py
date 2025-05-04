# coin name and price
def coin_worth(sentence):
    coin_value = {
        'penny': 0.01,
        'nickel': 0.05,
        'dime': 0.10,
        'quarter': 0.25
    }
    parts = sentence.split(' and ')
    total = 0.0
# for loop for finding coins and putting quantity together

    for part in parts:
        sections = part.strip().split()
        if len(sections) == 2:
            qty=int(sections[0])
            coin=sections[1].lower()
            if coin in coin_value:
                total += qty * coin_value[coin]
            else:
                print(f"Unknown coin: {coin}")
# show 2 decimal points
    return f"{total:.2f}"

# using test case

test_cases = [
    ("1 penny and 2 nickels", "0.11"),
    ("4 dimes and 7 quarters", "2.15"),
    ("1 quarter and 3 pennies", "0.28"),
    ("21 pennies and 17 dimes and 52 quarters", "14.91"),
    ("2 nickels and 5 dimes and 1 quarter", "0.80"),
    ("3 pennies and 4 quarters", "1.03"),
    ("10 dimes and 10 nickels", "1.50"),
    ("100 pennies", "1.00")
]
# testing cases
print("Sprint 1 Testing")
for i, (input_str, expected) in enumerate(test_cases):
    result=coin_worth(input_str)
    print(f"Test {i+1}: {input_str} -> {result} | {'PASS' if result == expected else 'FAIL'}")
