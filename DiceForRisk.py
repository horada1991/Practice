import random

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


print("Dice\n  Attacker:", "-".join(dice_a), "\n  Defender:", "-".join(dice_d))
