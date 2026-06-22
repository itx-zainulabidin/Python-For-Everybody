# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. The file is called 'regex_sum_42.txt' and is located in the same folder as this code.

import re

fhandle = open("regex_sum_2433808.txt","r")

total = 0
count = 0
for line in fhandle:
    numbers = re.findall("[0-9]+",line)
    for num in numbers:
        count += 1
        total += int(num)


print("Count:", count)
print("Total:", total)


