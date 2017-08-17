def mFun(*parm,base=3):
    result = 0
    for i in parm:
        result += i
    result *= base
    return result 

print(mFun(1,3,5,7,9,base=5))

