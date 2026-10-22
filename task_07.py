# Helper module: milkrate.py (included in this project folder)
# task_07.py imports it from the same folder.
import milkrate as mr

examples = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
for litres, fat, snf in examples:
    rate = mr.rate_per_litre(fat, snf)
    amount = mr.payout(litres, fat, snf)
    print(f"{litres:5} L | rate Rs {rate:5.2f} | pay Rs {amount:7.2f}")
