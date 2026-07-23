#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    binary_str = bin(n)[2:]
    
  
    consecutive_ones = [len(grupo) for grupo in binary_str.split('0')]
    
   
    print(max(consecutive_ones))