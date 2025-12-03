'''
pt 1: The ranges are separated by commas (,); 
each range gives its first ID and last ID separated by a dash (-).
you can find the invalid IDs 
by looking for any ID which is made only of some sequence of digits repeated twice.
None of the numbers have leading zeroes; 0101 isn't an ID at all. 
(101 is a valid ID that you would ignore.)

pt2 Now, an ID is invalid if it is made only of some sequence of digits
repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 
1212121212 (12 five times),
and 1111111 (1 seven times) are all invalid IDs.
'''
import re
with open('./inputday2.txt', 'r') as file:
    line = file.readline()
    IDS = line.strip()
    IDs = IDS.split(',')
    pattern = r"^([1-9]\d*)\1$"
    pattern2 = r"^([1-9]\d*)\1+$"
    invalid_id1 = 0
    invalid_id2 = 0
    for id in IDs:
        firstID, lastID = id.split('-')
        for i in range(int(firstID), int(lastID)+1):
            valid = re.fullmatch(pattern=pattern, string=str(i))
            if valid is None:
                continue
            else:
                invalid_id1+=i
    for id in IDs:
        firstID, lastID = id.split('-')
        for i in range(int(firstID), int(lastID)+1):
            valid = re.fullmatch(pattern=pattern2, string=str(i))
            if valid is not None:
                invalid_id2+=i

    print(invalid_id1)
    print(invalid_id2)