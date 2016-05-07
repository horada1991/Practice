import random

while 1:
    units_a = input("How many units attack: ")
    if units_a.isdigit():
        if int(units_a) > 0 and int(units_a) < 4:
            break
while 1:
    units_d = input("How many units defend: ")
    if units_d.isdigit():
        if int(units_d) > 0 and int(units_d) < 3:
            break

dice_a = []
dice_d = []

for i in range(0,3):
    dice_a.append(str(random.randrange(1,7)))
for i in range(0,2):
    dice_d.append(str(random.randrange(1,7)))

dice_a.sort()
dice_a.reverse()
dice_d.sort()
dice_d.reverse()
print("Dice\n  Attacker:", "-".join(dice_a), "\n  Defender:", "-".join(dice_d), "\n")

lost_d = 0
lost_a = 0
for i in range(0, len(dice_d)):
    if int(dice_d[i]) >= int(dice_a[i]):
        lost_a += 1
    else:
        lost_d += 1

print("Outcome:\n  Attacker: Lost", lost_a, "unit\n  Defender: Lost", lost_d, "unit\n")
