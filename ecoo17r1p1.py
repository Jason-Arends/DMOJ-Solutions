# https://dmoj.ca/problem/ecoo17r1p1

print('I hope a porcupine crawls up the ass of this problem and "Sonics".')

### THIS PROBLEM IS BAAAAAAAALLLLLLLLLS ###
"""  
Input Specification
The input contains 10 trips, at 3 lines of data per trip.

For each of the trips, the first line will show the cost of the trip as an integer ($50 to $ 50K ).
The next line contains four floating point numbers y1, y2, y3, y4(all between zero and one) and y1+y2+y3+y4 = 1)
representing the d of the total number of students from years 1 through 4 respectively.
The third line contains a single number , which contains the total number of students attending the brunch .
Note: You cannot have less than a whole person (e.g.,  people is the same as  person). Any missing or extra people should be removed from or added to the group with the highest percentage of c. There will always be exactly one group with the highest percentage of c.

Output Specification
Output YES if the student council needs to find other funding, and NO if the council has raised sufficient funds.

Sample input:
------
4000
0.5 0.2 0.1 0.2
400
6000
0.1 0.1 0.45 0.35
2000
------
Sample output:

YES
NO
"""
"------------------------------"

# UNACCEPTED * 9000

# brunch cost for each grade in order
k = [12, 10, 7, 5]

for i in range(10):
    a = int(input()) # cost of trip
    b = input() # a line of float nums that are actually a big string 
    c = int(input()) # total number of c

    d = [] # brunch attendee %s by seniority in a list/array.
    # split the string into a list of 4 strings and make them floats
    for i in b.split():
        d.append(float(i))

    e = []
    # calc number of students per year and check to see if floats are causing 3.4 persons to become just 3 [for example]
    for i in d:
        f = int(i * c)
        e.append(f)
    g = c - (sum(e))

    # if there ARE missing students, find which 'class' has the h c and add the "missing" students to it (per instructions).
    if g != 0:
        h = max(e)
        i = e.index(h)
        # replaces list with corrected one
        e [:] = [(h + g) if x == h else x for x in e]

    """
    print(e)
    print(h)
    print(g)
    #print(e.index(h))
    print(i)
    print(e)
    """

    # Profit math'd out 
    for i in range(len(e)):
        j = j + (k[i] * e[i])

    # We have to do more fundraising, yes or no? (half of brunch revenue enough to cover the cost of trip)
    if (j / 2) <= a:
        print('YES')
    else:
        print('NO')
print('YES')

print('NO')

# wrong solution FROM THE FUCKING BOOK (copied directly from Learn to Code by Solving Problems (zingaro 2021) pg 127 VERBATIM)
YEAR_COSTS = [12, 10, 7, 5]

for dataset in range(10):
    trip_cost = int(input())
    proportions = input().split()
    num_students = int(input())

    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])

    students_per_year = []

    for proportion in proportions:
        students = int(num_students * proportion)
        students_per_year.append(students)

    counted = sum(students_per_year)
    uncounted = students_per_year - counted
    most = max(students_per_year)
    where = students_per_year.index(most)
    students_per_year[where] = students_per_year[where] + uncounted

    total_raised = 0

    for i in range(len(students_per_year)):
        total_raised = total_raised + students_per_year[i] * YEAR_COSTS[i]

    if total_raised / 2 < trip_cost:
        print('YES')
    else:
        print('NO')

'------------------'
"""

Output Specification
Output YES if the student council needs to find other funding, and NO if the council has raised sufficient funds.

Sample input: (10 test cases of 3 lines each)
------
4000
0.5 0.2 0.1 0.2
400

6000
0.1 0.1 0.45 0.35
2000

504
[.2 .08 .4 .32]
125

50
.7 .1 .1 .1
9
------


Sample output:

YES
NO
"""
"------------------------------"
# brunch cost for each grade in order
YEAR_COSTS = [12, 10, 7, 5]

for i in range(10):
    trip_cost = int(input()) # cost of trip
    proportions = input() # a line of float nums that are actually a big string 
    num_students = int(input()) # total number of attendees

    percentages = [] # brunch attendee %s by seniority in a list/array.
    # split the string into a list of 4 strings and make them floats
    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])

    students_per_grade = []
    # calc number of students per year and check to see if floats are causing 3.4 persons to become just 3 [for example]
    for i in proportions:
        pupils = int(i * num_students)
        students_per_grade.append(pupils)
    missing_students = num_students - (sum(students_per_grade))

    # if there ARE missing students, find which 'class' has the most attendees and add the "missing" students to it (per instructions).
    if missing_students != 0:
        most = max(students_per_grade)
        hwere = students_per_grade.index(most)
        
        # replaces list with corrected one
        #students_per_grade [:] = [(most + missing_students) if x == most else x for x in students_per_grade]

    """
    print(students_per_grade)
    print(most)
    print(missing_students)
    #print(students_per_grade.index(most))
    print(where)
    print(students_per_grade)
    """
    total_raised = 0

    # Profit math'd out 
    for i in range(len(students_per_grade)):
        total_raised = total_raised + (students_per_grade[i] * YEAR_COSTS[i])

    # We have to do more fundraising, yes or no? (half of brunch revenue enough to cover the cost of trip)
    if (total_raised / 2) < trip_cost:
        print('YES')
    else:
        print('NO')   