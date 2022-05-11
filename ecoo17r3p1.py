# ECOO '17 R3 P1 - Baker Brie

# https://dmoj.ca/problem/ecoo17r3p
'''
4 5
4 3 2 4
3 3 2 1
8 2 4 1
2 2 4 3
9 3 2 3
-------
4 2
4 4 4 1
1 1 3 4
-------
4 3
4 3 2 4
4 4 4 1
5 1 5 2    '''
for i in range(1):
    eff_and_dee = input().split()
#    for digit in range(0, len(eff_and_dee)):
#        eff_and_dee[digit] = int(eff_and_dee[digit])
    franchisees = int(eff_and_dee[0])
    days = int(eff_and_dee[1])
    grid = []
    glo_bonuses = 0
    franchise_bonus = 0
    sales_franchise = 0
    daily_bonus = 0
    
    for i in range(days):
        row = input().split() #'4 3 2 4'.split() 
        for j in range(franchisees):
            row[j] = int(row[j])
        grid.append(row)
    
    for day in grid:
        total = sum(day)
        if total % 13 == 0:
            daily_bonus = daily_bonus + total // 13

    for col_index in range(franchisees):
        total = 0
        for row_index in range(days):
            #print (grid[col_index][row_index])
            #print('--')
            total = total + grid[row_index][col_index]
        if total % 13 == 0:
            franchise_bonus = franchise_bonus + total // 13
            

glo_bonuses = daily_bonus + franchise_bonus

print('-------')
print(daily_bonus)
print(franchise_bonus)
print(glo_bonuses)
print(grid)
    
#print(daily_bonus + franchise_bonus)    
# 
"""    for i in range(days):
        row = input().split() #'4 3 2 4'.split() 
        for j in range(franchisees):
            row[j] = int(row[j])
        grid.append(row)
        print(grid)
        
        [[4, 3, 2, 4], [4, 4, 4, 1], [5, 1, 5, 2]]
        """    

