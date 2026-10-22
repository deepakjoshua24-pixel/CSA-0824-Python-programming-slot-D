from decimal import Decimal

values = [10, 10.0, "10", True, [10, 8.5]]
for value in values:
    print(repr(value), "->", type(value).__name__)

print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

payments = ["33.40"] * 1000 + ["0.10"] * 3
float_total = sum(float(amount) for amount in payments)
decimal_total = sum((Decimal(amount) for amount in payments), Decimal("0.00"))
print("float total:", float_total)
print("Decimal total:", decimal_total)
print("float equality:", 0.1 + 0.2 == 0.3)
print("Decimal equality:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
