def fractiontodecimal(self,numerator,denominator):
    n,remainder = divmod(abs(numerator),abs(denominator))
    sign  = '-' if numerator*denominator<0 else ''
    remainders = {}
    result = [sign+str(n)]

    while remainder>0 and remainder not in remainders:
        remainders[remainder] = len(result)
        n,denominator = divmod(abs(remainder)*10,abs(denominator))
        result.append(str(n))

    if remainder in remainders:
        index = remainders[remainder]
        result.insert(index,'(')
        result.append(')')
    return ''.join(result).rstrip('.')
