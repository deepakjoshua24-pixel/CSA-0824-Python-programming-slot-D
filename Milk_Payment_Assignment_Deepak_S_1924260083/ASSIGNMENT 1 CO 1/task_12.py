from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
RATE_CARDS = {
    "regular": (Decimal("30.00"), Decimal("0.40"), Decimal("0.30")),
    "april_june": (Decimal("32.00"), Decimal("0.45"), Decimal("0.30")),
}

def payment(litres, fat, snf, season):
    """Calculate one entry using the selected season's rate card."""
    base, fat_value, snf_value = RATE_CARDS[season]
    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    rate = base + fat_steps * fat_value + snf_steps * snf_value
    return (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)

def ten_day_total(entries, season):
    """Return total payment with a Rs 0.50/L bonus above 500 litres."""
    litres_total = sum((entry[0] for entry in entries), Decimal("0"))
    total = sum((payment(*entry, season) for entry in entries), Decimal("0"))
    if litres_total > Decimal("500"):
        total += litres_total * Decimal("0.50")
    return total.quantize(CENT, rounding=ROUND_HALF_UP)

sample = [(Decimal("501"), Decimal("3.55"), Decimal("8.50"))]
for season in RATE_CARDS:
    print(season, "one-entry payment Rs", payment(*sample[0], season))
    print(season, "ten-day total incl. bonus Rs", ten_day_total(sample, season))
