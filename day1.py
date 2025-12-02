'''--- Day 1: Secret Entrance ---
The actual password is the number of times the dial is 
left pointing at 0 after any rotation in the sequence.
'''
import math

#read file
dial = 50 #start at 50 
hits_zero = 0
passes_zero = 0
with open('./inputday1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        m = line.strip()
        direction = m[0]
        x = int(m[1:])

        if direction == "L":
            signed_x = -x 
        elif direction == "R":
            signed_x = x
        

        start = dial
        end_raw = start + signed_x
        
        #calculate how many time we pass 
        #imma brute force this bitch 
        current = start
        step = 1 if direction == "R" else -1
        for _ in range(x):
            current =(current + step ) % 100
            if current == 0:
                passes_zero+=1
    
        dial = end_raw % 100 #use mod to loop so 99 goes back to 0 and vice versa.
        
        if dial == 0:
            hits_zero+=1


        
    print(hits_zero)
    print(passes_zero)