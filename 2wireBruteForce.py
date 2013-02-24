#Python 3
#Name: 2wire.py
#by: INIT_6
#Count from 0000000000 - 9999999999 skipping any numbers that repeat them selfs more then 3 times like 333

import sys

MAX_INT = 9990000000
BAD_PATTERNS = {x * 3 for x in '0123456789'}
# Use xrange for Python 2.7
for number in range(MAX_INT):
    int_string = str(number).rjust(10, '0')
    if any(pattern in int_string for pattern in BAD_PATTERNS):
        continue
    print ( str(number).rjust(10, '0') )
