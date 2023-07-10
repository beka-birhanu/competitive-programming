def superDigit(n, k):
    if len(n)>1:
        sum = 0
        for x in n:
            sum += int(x)
        return superDigit(str(sum)*k,1)
    return int(n)
