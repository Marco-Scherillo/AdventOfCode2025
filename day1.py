'''--- Day 1: Secret Entrance ---
The actual password is the number of times the dial is 
left pointing at 0 after any rotation in the sequence.
'''

#read file
dial = 50 #start at 50 
counter = 0
with open('./inputday1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        move = line.strip()
        direction = ""
        value = ""
        for char in move:
            if char.isalpha():
                direction = char
            elif char.isdigit():
                value+= char
        if direction == "L":
            dial = (dial - int(value)) % 100 #use mod to loop so 99 goes back to 0 and vice versa.
        elif direction == "R":
            dial = (dial + int(value)) % 100
        if dial == 0:
            counter+=1
    print(counter)