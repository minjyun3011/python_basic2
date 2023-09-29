import random

dice_number = int(input("サイコロの面の数は？: "))
trial_number = int(input("何回振りますか？: "))
results = []

for i in range(trial_number):
    roll_result = random.randint(1, dice_number)
    results.append(roll_result)

print(results)