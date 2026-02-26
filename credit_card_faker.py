from faker import Faker
import random, time
import pandas as pd

fake = Faker()

def luhn_validate(card_number):
    # Remove any spaces or hyphens
    card_number = card_number.replace(' ', '').replace('-', '')
    
    # Convert to list of integers
    digits = [int(d) for d in card_number]
    
    # Double every second digit from right to left
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
            
    # Sum all digits
    total = sum(digits)
    
    # Check if divisible by 10
    return "Valid" if total % 10 == 0 else "Invalid"

# Define the columns with new Luhn Validation column
columns = [
    "TransactionID", "CardNumber", "LuhnValidation", "CardHolderName", "TransactionDate",
    "TransactionAmount", "MerchantName", "MerchantAddress", "PhoneNumber",
    "TransactionType", "Remarks"
]

# Generate fake data
data = []
print("started processing 10 rows")

print(time.time())
for _ in range(10):
    transaction = [
        fake.uuid4(),
        fake.credit_card_number(card_type=["visa", "mastercard", "amex"][random.randint(0, 2)]),
        "",  # Placeholder for Luhn validation
        fake.name(),
        fake.date_time_this_year(),
        round(random.uniform(1.0, 1000.0), 2),
        fake.company(),
        fake.address(),
        fake.phone_number(),
        random.choice(["Purchase", "Refund", "Withdrawal"]),
        fake.text(max_nb_chars=20)
    ]
    
    # Add Luhn validation result
    transaction[2] = luhn_validate(transaction[1])
    
    # Add some prefix and trailing spaces, and non-ascii characters
    transaction[3] = " " + str(transaction[3]) + " "  # Note: index changed from 2 to 3
    transaction[6] = " " + str(transaction[6]) + " "
    transaction[7] = " " + str(transaction[7]) + " "
    transaction[10] = str(transaction[10]) + " "  # Note: index changed from 9 to 10
    data.append(transaction)

# Convert to DataFrame
df = pd.DataFrame(data, columns=columns)

print(df)