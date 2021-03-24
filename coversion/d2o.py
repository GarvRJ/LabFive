import math


def do(n):
    oct=0
    p=0
    while(n>=1):
        if(n%8!=0):
            oct+=(n%8)*(10**p)
        p+=1
        n=math.floor(n/8)
    return oct