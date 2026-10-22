# Task 1: identify and calculate the data for one farmer
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

farmer_id = "F102"       # text identifier
litres = 10.0             # fractional quantity
fat = 4.2                 # fractional percentage
snf = 8.7                 # fractional percentage
shift = "Morning"         # text label

fat_steps = round((fat - STANDARD_FAT) / 0.1)
snf_steps = round((snf - STANDARD_SNF) / 0.1)
rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
amount = round(litres * rate, 2)
ten_day_total = amount    # one sample entry

print("Farmer:", farmer_id, "Shift:", shift)
print(f"Rate: Rs {rate:.2f}/L | Amount: Rs {amount:.2f}")
print(f"Ten-day total: Rs {ten_day_total:.2f}")
