def dh(n):
    hex=""
    if (n < 0):
        return 0
    elif (n<=1):
        return n
    else:
        x =(n%16)
        if (x < 10):
            hex+=x.toString,
        if (x == 10):
            hex+="A"
        if (x == 11):
            hex+="B"
        if (x == 12):
            hex+="C"
        if (x == 13):
            hex+="D"
        if (x == 14):
            hex+="E"
        if (x == 15):
            hex+="F"
        dh( n / 16 )
        return hex