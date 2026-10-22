def calculate_payment(litres_text, fat_text, snf_text):
    """Convert three text inputs, validate them and return a payment."""
    try:
        litres = float(litres_text.strip())
        fat = float(fat_text.strip())
        snf = float(snf_text.strip())
    except ValueError:
        return None, "Enter numeric values such as 8.5."
    if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
        return None, "Quantity or milk percentage is outside the allowed range."
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
    return round(litres * rate, 2), "OK"

# input() always gives text; these sample strings show the same conversion path.
for sample in [("8.5", "4.2", "8.7"), ("8,5", "4.2", "8.7"), ("eight", "4.2", "8.7")]:
    amount, message = calculate_payment(*sample)
    if amount is None:
        print("Invalid:", sample[0], "-", message)
    else:
        print(f"Payment: Rs {amount:8.2f}")
