BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

litres = 10
print("litres:", litres, type(litres).__name__)
litres = "ten"
print("same name reassigned:", litres, type(litres).__name__)

fat, snf = 4.2, 8.7
fat, snf = snf, fat
print("after swap - fat:", fat, "snf:", snf)

rate_card = {"base": BASE_RATE, "fat_step": FAT_STEP_VALUE,
             "snf_step": SNF_STEP_VALUE}
print("rate card:", rate_card)
