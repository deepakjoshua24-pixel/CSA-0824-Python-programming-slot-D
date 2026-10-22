def payment(litres, fat, snf):
    """Return a rounded payment or raise ValueError for invalid input."""
    if litres < 0:
        raise ValueError("litres cannot be negative")
    if not 2.0 <= fat <= 7.0 or snf < 0:
        raise ValueError("fat or SNF is outside the allowed range")
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
    return round(litres * rate, 2)

cases = [("standard", (10, 3.5, 8.5), 300.00),
         ("above standard", (8.5, 4.2, 8.7), 283.90),
         ("lowest fat", (1, 2.0, 8.5), 24.00),
         ("highest fat", (1, 7.0, 8.5), 44.00)]
for name, values, expected in cases:
    actual = payment(*values)
    assert actual == expected, f"{name}: expected {expected}, got {actual}"
    print(f"PASS {name:15} expected Rs {expected:6.2f} actual Rs {actual:6.2f}")
for values in [(-1, 3.5, 8.5), (1, 7.1, 8.5)]:
    try:
        payment(*values)
    except ValueError as error:
        print("PASS invalid input:", error)
