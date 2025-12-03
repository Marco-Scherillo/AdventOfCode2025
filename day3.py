'''
The batteries are arranged into banks; each line of digits
in your input corresponds to a single bank of batteries. Within each bank,
you need to turn on exactly two batteries; the joltage that the bank
produces is equal to the number formed by the digits on the batteries you've turned on.

Pt1: find the largest possible joltage each bank can produce.

PT2: Now, you need to make the largest joltage by turning on exactly
twelve batteries within each bank.
The joltage output for the bank is still the number formed by the digits of the batteries 
you've turned on; the only 
difference is that now there will be 12 digits in each bank's joltage output instead of two.
'''

def find_highest_jultage(bank):
    #fuck it O(n^2) it is
    largest_sum = 0
    n = len(bank)
    for i in range(n):
        for j in range(i+1, n):
            current = int(f"{bank[i]}{bank[j]}")
            if largest_sum < current:
                largest_sum = current
    return largest_sum

def find_k_largest(bank, k): # greedy apreach 
    result = []
    start = 0
    k_remaining = k

    for i in range(k):
        end = len(bank) - (k_remaining - 1) #update end 
        best_digit = -1
        best_index = -1
        for j in range(start, end):
            if int(bank[j]) > best_digit:
                best_digit = int(bank[j])
                best_index = j
        result.append(str(best_digit))
        start = best_index + 1 #update start
        k_remaining-=1 #decrease k 
    return "".join(result)


        





with open('./inputday3.txt', 'r') as file:
    lines = file.readlines()
    joltage = 0
    for line in lines:
        digits = list(line.strip())
        joltage+=find_highest_jultage(digits)
    print(f"pt1: {joltage}")

    #Part 2
    #greedy selection
    joltage=0
    for line in lines:
        digits = list(line.strip())
        joltage+= int(find_k_largest(digits, 12))
    print(f"pt2: {joltage}")


