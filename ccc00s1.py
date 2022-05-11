# CCC '00 S1 - Slot Machines

marthas_qs = int(input())
mach_35 = int(input())
mach_60 = int(input())
mach_10 = int(input())

plays = 0

while marthas_qs != 0:
    
    plays += 1
    mach_35 += 1
    marthas_qs -= 1
    if mach_35 == 35:
        marthas_qs += 30
        mach_35 = 0

    
    plays += 1
    mach_60 += 1
    marthas_qs -= 1
    if mach_60 == 60:
        marthas_qs += 60
        mach_60 = 0
    
    plays += 1
    mach_10 += 1
    marthas_qs -= 1
    if mach_10 == 10:
        marthas_qs += 9
        mach_10 = 0
    
print(f'Martha plays {plays} times before going broke.')

'----------------------'    
marthas_qs = int(input())
mach_35 = int(input())
mach_100 = int(input())
mach_10 = int(input())

machine = 0
plays = 0 

while marthas_qs >= 1:
    marthas_qs -= 1
    
    if machine == 0:
        mach_35 += 1
        if mach_35 == 35:
            mach_35 = 0
            marthas_qs += 30

    elif machine == 1:
        mach_100 += 1
        if mach_100 == 100:
            mach_0 = 0
            marthas_qs += 60
    
    elif machine == 2:
        mach_10 += 1
        if mach_10 == 10:
            mach_10 = 0
            marthas_qs += 9      
    plays += 1
    machine += 1
    if machine == 3:
        machine = 0
        
print(f'Martha plays {plays} times before going broke.')
'----------------------'    

marthas_qs = int(input())
mach_35 = int(input())
mach_100 = int(input())
mach_10 = int(input())

plays = 0 

while marthas_qs >= 1:
    marthas_qs -= 1
    
    if plays % 3 == 0:
        mach_35 += 1
        if mach_35 == 35:
            mach_35 = 0
            marthas_qs += 30

    elif plays % 3  == 1:
        mach_100 += 1
        if mach_100 == 100:
            mach_0 = 0
            marthas_qs += 60
    
    elif plays % 3  == 2:
        mach_10 += 1
        if mach_10 == 10:
            mach_10 = 0
            marthas_qs += 9      
    plays += 1
    machine += 1
    if machine == 3:
        machine = 0
        
    
print(f'Martha plays {plays} times before going broke.')
'----------------------'    

marthas_qs = int(input())
mach_35 = int(input())
mach_100 = int(input())
mach_10 = int(input())

plays = 0 

while marthas_qs >= 1:
    marthas_qs -= 1
    
    if plays % 3 == 0:
        mach_35 += 1
        if mach_35 == 35:
            mach_35 = 0
            marthas_qs += 30

    elif plays % 3  == 1:
        mach_100 += 1
        if mach_100 == 100:
            mach_100 = 0
            marthas_qs += 60
    
    elif plays % 3  == 2:
        mach_10 += 1
        if mach_10 == 10:
            mach_10 = 0
            marthas_qs += 9      
    plays += 1
    
print(f'Martha plays {plays} times before going broke.')
