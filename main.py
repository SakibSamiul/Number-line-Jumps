
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):

    x = (x2 - x1)
    v = (v1 - v2)

    if (x and v) != 0:
        
        r = x % v
        if r == 0:
            if x2 > x1 and v1 > v2:
                print("YES")
            elif x2 > x1 and v1 < v2:
                print("NO")
            else:
                print("NO")
            
        else:
            
            print("NO")
    else:
        print("NO")
   
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
