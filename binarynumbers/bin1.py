def isOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True

print("isOdd(42)    should be  False:", isOdd(42))
print("isOdd(43)    should be  True:", isOdd(43))

def numToBinary(N):
    """returns the binary number
    """
    if N == 0:
        return ''
    elif N % 2 == 1:
        return numToBinary(N // 2) + '1'
    else:
        return numToBinary(N // 2) + '0'


print("numToBinary(0)      should be  '':",  numToBinary(0))
print("numToBinary(42)     should be  '101010':",  numToBinary(42))

def binaryToNum(S):
    """converts a binary of a number to a decimal
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return   binaryToNum(S[:-1]) * 2 + 1

    else: # last digit must be '0'
        return   binaryToNum(S[:-1]) * 2 + 0

# tests

print("binaryToNum('')     should be  0:",  binaryToNum(''))
print("binaryToNum('101010') should be  42:",  binaryToNum('101010'))

def increment(S):
    """returns the next integer in binary numbers"""
    if S == '':
        return 0
    elif S == '11111111':
        return '00000000'
    else:
        n = binaryToNum(S)
        x = n+1
        y = numToBinary(x)
        return (len(S) - len(y)) * '0' + y

print("increment('00101001')    should be  00101010:", increment('00101001'))
print("increment('00000011')    should be  00000100:", increment('00000011'))
print("increment('11111111')    should be  00000000:", increment('11111111'))

def numToTernary(N):
    if N == 0:
        return ''
    elif N % 3 == 2:
        return numToTernary(N // 3) + '2'
    elif N % 3 == 1:
        return numToTernary(N // 3) + '1'
    else:
        return numToTernary(N // 3) + '0'
    
def ternaryToNum(S):
    if S == '':
        return 0
    elif S[-1] == '2':
        return ternaryToNum(S[:-1]) * 3 + 2
    elif S[-1] == '1':
        return ternaryToNum(S[:-1]) * 3 + 1
    else:
        return ternaryToNum(S[:-1]) * 3 + 0

    
