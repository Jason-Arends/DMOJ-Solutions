# https://dmoj.ca/problem/ccc18s1

"""
Input Specification
The first line will contain the number  , the number of villages. On the next  lines there will be one integer per line, where the  line will contain the integer , the position of the  village . All villages are at distinct positions.

Output Specification
Output the smallest neighbourhood size with exactly one digit after the decimal point.

Sample Input
5
16
0
10
4
15
Sample Output
3.0
"""
'''test cases'''
# b = [20,50,4,19,15,1]
# a = [5 16 0 10 4 15]
"-----------------------"
vill_count = int(input())

# get town positions and put them in a list and order it
vill_lst = []
for i in range(vill_count):
    vill_positions = int(input())
    vill_lst.append(vill_positions)
vill_lst.sort()

town_size = 0.0 # composite size of town 

# I need to give my loop something to compare its maths against. 
min_size = 2000000000 #Biggest size allowed by input params


itters = 1 # "starting at index one instead of zero so we can get both left and right measurements
while itters < vill_count - 1:
#for i in range(1, vill_count - 1):
    left = ((vill_lst[itters] - vill_lst[itters - 1]) / 2)
    right = ((vill_lst[itters + 1] - vill_lst[itters]) / 2)
    town_size = left + right 
# If measured town is smaller than smallest town, it becomes smallest.
    if town_size < min_size: 
        min_size = town_size
    itters += 1

print(min_size)
#print(sorted(a))
#print(sorted(b))
"-----------------------"

"-----------------------"
" I managed to rewrite the loop to add all town sizes to a list, then used the min function to pull out the smallest "


vill_count = int(input())

# get town positions and put them in a list and order it
vill_lst = []
for i in range(vill_count):
    vill_positions = int(input())
    vill_lst.append(vill_positions)
vill_lst.sort()

town_size = 0.0 # composite size of town 

# I need to give my loop something to compare its maths against. 
#min_size = 2000000000 #Biggest size allowed by input params


itters = 1 # "starting at index one instead of zero so we can get both left and right measurements
size_lst = [] # storing calc'd values
while itters < vill_count - 1:
#for i in range(1, vill_count - 1):
    left = ((vill_lst[itters] - vill_lst[itters - 1]) / 2)
    right = ((vill_lst[itters + 1] - vill_lst[itters]) / 2)
    town_size = left + right 
    size_lst.append(town_size)
    itters += 1
"""# If measured town is smaller than smallest town, it becomes smallest.
    if town_size < min_size: 
        min_size = town_size"""
   

print(min(size_lst))
#print(sorted(a))
#print(sorted(b))