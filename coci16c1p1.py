# COCI '16 Contest 1 #1 Data Plan
# 1st attempt 
"""
mb_per_mo = int(input())
n_months = int(input())

rolling_over = 0
for i in range(n_months):
    mb_used = int(input())
    rolling_over = (mb_per_mo + rolling_over) - mb_used
    np1_months = mb_per_mo + rolling_over
print(np1_months)
"""
'----------------------'    
# Second Attempt
mb_per_mo = int(input())
n_months = int(input())

mb_piggyB = mb_per_mo * (n_months + 1)

for i in range(n_months):
    mb_used = int(input())
    mb_piggyB = mb_piggyB - mb_used
    
print(mb_piggyB)