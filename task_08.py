entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total = 0.0
for number, (litres, fat, snf) in enumerate(entries, start=1):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
    payment = round(litres * rate, 2)
    total = round(total + payment, 2)
    print(f"Entry {number}: payment Rs {payment:.2f}; running total Rs {total:.2f}")
print(f"Ten-day total: Rs {total:.2f}")
