# CCgen

This Python script generates fake credit card data in JSON format. It creates a variety of credit card types (Visa, MasterCard, Amex, and Discover), including randomly generated card numbers, CVVs, expiration dates, and names. The generated JSON file is human-readable, with proper formatting.

---

## Features

- Generates fake credit card data, including:
  - Card type (Visa, MasterCard, Amex, Discover)
  - Card number (valid based on Luhn's algorithm)
  - CVV
  - Expiry date
  - Randomly generated name (e.g., "John Doe")
  
- The generated JSON is formatted for easy reading, with **indented** structure.
  
- The script can generate **any amout ofJSON** data.

---

## Requirements

This script does **not** require any external dependencies. It uses only built-in Python libraries:

- `random`
- `string`
- `json`

There are no additional installation steps or external libraries required.

---

## Installation

1. **Clone the repository** or download the `ccs.py` script.

2. **Ensure you have Python 3.x installed**.

3. **Run the script**:
   - Open a terminal and navigate to the directory where the script is located.
   - Run the following command:
     ```bash
     python3 ccs.py
     ```

   The script will generate a file named `ccs.json` in the same directory.

---

### Generating Fake Credit Card Data

To generate fake credit card data:

1. **Run the script** by executing the command:
   ```bash
   python3 ccs.py
