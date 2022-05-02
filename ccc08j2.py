# CCC '08 J2 - Do the Shuffle

songs = 'ABCDE'

#if button_to_press == 1:


button = int(input())
times =  int(input())


while button != 4:
    # Read button
    # Read # of presses
    # Process presses

# Button 1: moves first song to last position
    if button == 1:
        for press in range(times):
            songs = songs[1:] + songs[0]
        button= int(input())
        times =  int(input())

# Button 2: moves song in last to 1st position
    elif button == 2:
        for press in range(times):
            songs = songs[4] + songs[0:4]
        button= int(input())
        times =  int(input())

# Button 3: swaps songs in 1st and 2nd position
    elif button == 3:
        for press in range(times):
            songs = songs[1] + songs[0] + songs[2:]
        button= int(input())
        times =  int(input())

# Button 4: stop rearranging; play (ends script when 4 is selected)

print(f'{songs[0]} {songs[1]} {songs[2]} {songs[3]} {songs[4]}')