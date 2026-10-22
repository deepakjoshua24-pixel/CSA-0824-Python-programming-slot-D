from decimal import Decimal
from time import perf_counter

for count in (300, 6000, 150000):
    amounts = ["33.40"] * count
    start = perf_counter()
    float_total = sum(float(value) for value in amounts)
    float_seconds = perf_counter() - start
    start = perf_counter()
    decimal_total = sum((Decimal(value) for value in amounts), Decimal("0.00"))
    decimal_seconds = perf_counter() - start
    print(f"n={count:6} float={float_total:.2f} Decimal={decimal_total:.2f}")
    print(f"          difference={float_total - float(decimal_total):.8f}; "
          f"time float={float_seconds:.6f}s Decimal={decimal_seconds:.6f}s")
