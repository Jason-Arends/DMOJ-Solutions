# COCI '12 Contest 5 #1 Ljestvica

notes = str(input())
c_dur = 0
a_mol = 0
unpiped = ''
for i in notes:
    if i != '|':
        unpiped = unpiped + i

for note in unpiped:
    if note == 'C' or note == 'F' or note == 'G': 
        c_dur += 1
    elif note == 'A' or note == 'D' or note == 'E':
        a_mol += 1
if a_mol > c_dur:
    print('A-mol')
elif a_mol < c_dur:
    print('C-dur')