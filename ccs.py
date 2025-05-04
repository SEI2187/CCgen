import json
import random
import string

# Card types
CARD_TYPES = {
    "Visa": {"prefix": ["4"], "length": 16},
    "MasterCard": {"prefix": ["51", "52", "53", "54", "55"], "length": 16},
    "Amex": {"prefix": ["34", "37"], "length": 15},
    "Discover": {"prefix": ["6011", "65"], "length": 16},
}

# Generate a random name
def generate_fake_name():
    first_names = ["John", "Jane", "Alex", "Chris", "Mary", "Paul", "Kelsey", "Taylor", "Jordan", "Pat"]
    last_names = ["Smith", "Doe", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Martinez", "Davis", "Miller"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Luhn checksum algorithm for validating card number
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd = digits[-1::-2]
    even = digits[-2::-2]
    total = sum(odd)
    for d in even:
        total += sum(digits_of(d * 2))
    return str((10 - (total % 10)) % 10)

# Generate a fake card number
def generate_card_number(card_type):
    info = CARD_TYPES[card_type]
    prefix = random.choice(info["prefix"])
    length = info["length"]
    number = prefix
    while len(number) < length - 1:
        number += str(random.randint(0, 9))
    number += luhn_checksum(number)
    return number

# Generate fake card information
def generate_fake_card():
    card_type = random.choice(list(CARD_TYPES.keys()))
    return {
        "type": card_type,
        "number": generate_card_number(card_type),
        "cvv": ''.join(random.choices("0123456789", k=3 if card_type != "Amex" else 4)),
        "expiry": f"{random.randint(1, 12):02d}/{random.randint(26, 30)}",
        "name": generate_fake_name()  # Use our simple name generator
    }

# Save fake cards to a JSON file
def save_to_json(file_path, max_bytes=1_000_000_000):
    count = 0
    with open(file_path, 'w') as f:
        f.write('[\n')
        while True:
            entry = generate_fake_card()
            json_str = json.dumps(entry, indent=2)
            if f.tell() + len(json_str.encode('utf-8')) + 2 >= max_bytes:
                break
            if count > 0:
                f.write(',\n')
            f.write(json_str)
            count += 1
            if count % 1000 == 0:
                print(f"Getting {count} cards, file size: {f.tell() / (1024 * 1024):.2f} MB")
        f.write('\n]')
    print(f"\n✅ Done! Generated {count} fake cards in {file_path}")

if __name__ == "__main__":
    save_to_json("ccs.json")
