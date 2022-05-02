#CCC '11 S1 - English or French?

no_lines = int(input())

lil_esses = 0
lil_tees = 0
big_esses = 0
big_tees = 0

for i in range(no_lines):
    line = str(input())
    lil_tees = lil_tees + line.count('t') 
    big_tees = big_tees + line.count('T') 
    lil_esses = lil_esses + line.count('s')
    big_esses = big_esses + line.count('S')
 
all_tees = big_tees + lil_tees
all_esses = big_esses + lil_esses

if all_esses >= all_tees:
    print('French')
else:
    print('English')
print(all_tees)
print(all_esses)
