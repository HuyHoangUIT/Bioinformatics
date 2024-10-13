import os
import sys

def HammingDistance(String1, String2):
    count = 0
    
    for i in range (len(String1)):
        if String1[i] != String2[i]:
            count += 1
    return count