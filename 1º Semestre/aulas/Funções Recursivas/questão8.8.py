def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(mdc(12,8))

def mmc(a,b):
    return a*b/mdc(a,b)

print(mmc(12,9))
