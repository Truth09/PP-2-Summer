import re
import datetime

with open("raw.txt", "r", encoding="utf-8") as file:
	text = file.read()

# Extract all prices from the receipt

all_costs = re.findall(r"Стоимость\s*\n([0-9 ]+,\d{2})", text)				# Literal word + whitespace + new line + Capture Group( Any number + Space + "," + two decimals )

# Find all product names

product_names = re.findall(r"\d+\.\s+([^\n]+)", text)		# Any number + "." + whitespace + Capture Group( Any characters until new line )

# Calculate total amount

total = sum(float(price.replace(" ", "").replace(",", ".")) for price in all_costs)	# For price in all_costs, replace space with nothing, and replace "," with "." so it can be converted to float

# Extract date and time information

time = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)		# Literal word + whitespace + Capture Group( DD.MM.YYYY ) + whitespace + Capture Group( HH:MM:SS )

if time:
    date = time.group(1)
    time = time.group(2)

# Find payment method

payment_method = re.findall(r"(Банковская карта|Наличные|Карта)", text)		# Capture Group( Match one of the payment methods: Bank card / Cash / Card )

# Create a structured output (JSON or formatted text)

print("				Receipt Information")
print("--------------------------------------------------------------------------------")

for i in range(0, len(product_names)):
	print(f"{i+1}. {product_names[i]}")
	print(f"{all_costs[i]} KZT")

print(f"\nTotal: {total:.2f} KZT\n")

print(f"Date and Time: {date} / {time} \n")
print(f"Payment Method: {payment_method[0]}")
