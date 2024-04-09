"""
Memory eater python program
Consume one GB of heap memory in each iteration
"""

import time

lst=[]

# Consume One GB for each iteration
for item in range(10):
    # append bytearray object to list to retain in memory
    lst.append(bytearray(1024*1024*1000))
    time.sleep(3)

print('before end program')
time.sleep(50)
