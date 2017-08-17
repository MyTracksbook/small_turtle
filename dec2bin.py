def dec2bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
    #return temp
    
    while temp:
        result +=str(temp.pop())

    return result
print(dec2bin(62))
