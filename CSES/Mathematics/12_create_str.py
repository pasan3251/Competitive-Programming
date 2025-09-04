# This code cannot work properly only when n is small



import math                         # use to get factorials

from collections import Counter     # use to count hashable Obj like letters,words,numbers

string = input()                    
str_len = len(string)

letter_count = Counter(string)      # creates a dictionary with letters and each count

# max string count is when all characters are distinct 
max_count = math.factorial(str_len)

# we divide the max count by the factorials of repeated characters' individual counts
for key, value in letter_count.items():
    if value > 1:
        max_count /= math.factorial(value)
        
        
print(int(max_count % (10**9 + 7)))