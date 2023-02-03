
#print(s[-1]+s[:len(s)-1])
#o/p:bcda
##Direct=0::left Direction// Direction=1::Right Direction
s='abcd'
def shiftString(str,noOfShift, direction):
    res=''
    for i in range(0,noOfShift):
        if direction==0:
            res+=str[1::]+str[0] ##Left Shift
        else:
            res+=str[-1]+str[:len(str)-1] ##Right Shift
        yield res
        str=res
        res =''
res=shiftString(s,4,1)
for ch in res:
    print(ch)