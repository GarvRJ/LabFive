def db(n):
    bin=0
    p=0
    while(n>=1):
        if(n%2!=0):
            bin+=10**p
        p+=1
        n/=2
    return bin