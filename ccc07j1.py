# CCC '07 J1 - Who is in the Middle?

#input from grader ints all less than 100
bowl_1  = int(input())
bowl_2  = int(input())
bowl_3  = int(input())

#create list to sort
bowl_list = [bowl_1, bowl_2, bowl_3]
#sort the list
bowl_list.sort()
#return mama's bowl
print(bowl_list[1])

moves = str(input())
location = 1