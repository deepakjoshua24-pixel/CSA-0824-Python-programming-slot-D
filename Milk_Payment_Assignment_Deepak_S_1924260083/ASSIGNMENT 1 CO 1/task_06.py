BASE_RATE = 30.00

def rate_per_litre(fat, snf):
    """Return the milk rate per litre for the supplied percentages."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * 0.40 + snf_steps * 0.30, 2)

def payout(litres, fat, snf):
    """Return the payment for one milk entry."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(entries):
    """Return the sum of payments in a list of (litres, fat, snf) entries."""
    total = 0.0
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return round(total, 2)

entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
for entry in entries:
    print(f"{entry[0]:5} L -> Rs {payout(*entry):.2f}")
print(f"Ten-day total: Rs {ten_day_total(entries):.2f}")
