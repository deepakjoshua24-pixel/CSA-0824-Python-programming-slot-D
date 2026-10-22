import math

BASE_RATE = 30.00
fat, snf, litres = 4.2, 8.7, 8.5
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = round(BASE_RATE + fat_steps * 0.40 + snf_steps * 0.30, 2)
amount = round(litres * rate, 2)
print("fat steps:", fat_steps, "snf steps:", snf_steps)
print(f"rate Rs {rate:.2f}; payment Rs {amount:.2f}")

print("0.1 + 0.2:", 0.1 + 0.2)
print("(4.2 - 3.5) / 0.1:", (4.2 - 3.5) / 0.1)
print("-7 / 2: round, int, floor =", round(-7 / 2), int(-7 / 2), math.floor(-7 / 2))
print("precedence: -2**2 =", -2**2, "but (-2)**2 =", (-2)**2)
print("valid fat:", 2.0 <= 4.2 <= 7.0)
