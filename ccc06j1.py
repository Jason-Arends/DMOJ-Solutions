# CCC '06 J1 - Canadian Calorie Counting
brgr_pik = int(input())
side_pik = int(input())
drnk_pik = int(input())
dsrt_pik = int(input())

total_cals = 0

if brgr_pik == 1:
    total_cals += 461 # burger
elif brgr_pik == 2:
    total_cals += 431 # fishburger
elif brgr_pik == 3:
    total_cals += 420 # veg burger
else:
    total_cals += 0  #none burger


if side_pik == 1:
    total_cals += 100 # fries
if side_pik == 2:
    total_cals += 57 # baked 'tato
if side_pik == 3:
    total_cals += 70 # salad
else:
    total_cals += 0 # no side


if drnk_pik == 1:
    total_cals += 130 # soft drank
if drnk_pik == 2:
    total_cals += 160 # juice
if drnk_pik == 3:
    total_cals += 118 # milk
else:
    total_cals += 0 # none drink


if dsrt_pik == 1:
    total_cals += 167 # apple pie
if dsrt_pik == 2:
    total_cals += 266 # sundae
if dsrt_pik == 3:
    total_cals += 75 # fruit cup
else:
    total_cals += 0 # no dessert

print(f'Your total Calorie count is {total_cals}.')