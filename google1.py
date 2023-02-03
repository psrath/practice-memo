ar=[1,3,4]
def resarr(ar):
    print(len(ar))
    carry = 1
    res = []
    for i in range(len(ar)-1,-1,-1):
        #print(ar[i])
        total = ar[i]+1
        if total == 10:
            carry =1
        else:
            carry=0
        res[i]=total % 10
    return res        
print(resarr(ar))