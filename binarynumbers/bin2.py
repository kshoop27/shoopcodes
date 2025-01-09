def numToBaseB(N, B):
    if N == 0:
        return ''
    else:
        return str(numToBaseB(N//B, B)) + str(N % B) 
    
assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'

def baseBToNum(S, B):
    if S == '':
        return 0
    else:
        return int(B * baseBToNum(S[:-1], B)) + int(S[-1]) 

def baseToBase(B1, B2, s_in_B1):
    x = baseBToNum(s_in_B1, B1)
    return numToBaseB(x, B2)
    
assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'

def add(S, T):
    x = baseBToNum(S, 2)
    y = baseBToNum(T, 2)
    R = x + y
    return numToBaseB(R, 2)

def addB(S, T):
   """Takes S and T which are binary nubers and adds them together and returns the binary number"""
   if S == '':
        return T 
   elif T == '':
       return S
   elif S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'   # 0 + 0 == 0
   elif S[-1] == '1' and T[-1] == '0':
       return addB(S[:-1], T[:-1]) + '1'
   elif S[-1] == '0' and T[-1] == '1':
       return addB(S[:-1], T[:-1]) + '1'
   elif S[-1] == '1' and T[-1] == '1':
       return addB(addB(S[:-1], '1'), T[:-1]) +'0'
   
def frontNum(S):
    if len(S) <= 1:
        return len(S)
    elif S[0] == S[1]:
        return frontNum(S[1:]) + 1
    else:
        return 1
 
def compress(S):
    if S == '':
        return ''
    elif S[0] == '1':
        return '1' + (7 - len(numToBaseB(frontNum(S), 2))) * '0' + numToBaseB(frontNum(S), 2) + compress(S[frontNum(S):])
    elif S[0] == '0':
        return '0' + (7 - len(numToBaseB(frontNum(S), 2))) * '0' + numToBaseB(frontNum(S), 2) + compress(S[frontNum(S):])

def uncompress(C):
    h = baseBToNum(C[1:8], 2)
    if C == '':
        return ''
    elif C[0] == '0':
        return h * '0' + uncompress(C[8:])
    elif C[0] == '1':
        return h * '1' + uncompress(C[8:])
    
    
   

   
    
   




