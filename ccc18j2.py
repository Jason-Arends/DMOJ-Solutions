# CCC '18 J2 - Occupy parking

num_spaces = int(input())
day_1 = str(input())
day_2 = str(input())

occupied = 0

for i in range(num_spaces):
    if day_1[i] == 'C' and day_2[i] == "C":
        occupied += 1

print(occupied)