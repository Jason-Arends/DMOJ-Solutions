#DMOPC '16 Contest 1 P0 - C.C. and Cheese-kun

width = int(input())
x_cheese = int(input())
x_happy = str('test')

if width == 3 and x_cheese >= 95:
    x_happy = 'absolutely'
elif width == 1 and x_cheese <= 50:
    x_happy = 'fairly'
else:
    x_happy = 'very'

print(f'C.C. is {x_happy} satisfied with her pizza.')