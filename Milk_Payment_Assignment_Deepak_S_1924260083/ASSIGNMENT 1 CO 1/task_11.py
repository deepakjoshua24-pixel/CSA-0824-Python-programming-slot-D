from decimal import Decimal, ROUND_HALF_UP

BASE = Decimal("30.00")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")
CENT = Decimal("0.01")

def payment(litres_text, fat_text, snf_text):
    """Validate text inputs and return an exact two-decimal payment."""
    litres, fat, snf = map(Decimal, (litres_text, fat_text, snf_text))
    if litres < 0 or not Decimal("2.0") <= fat <= Decimal("7.0") or snf < 0:
        raise ValueError("milk entry is outside the allowed range")
    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"))
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"))
    rate = BASE + fat_steps * FAT_STEP + snf_steps * SNF_STEP
    return (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)

print("Recommended payment: Rs", payment("8.5", "4.2", "8.7"))
