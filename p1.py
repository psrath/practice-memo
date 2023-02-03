lt = [6,5,2,3,7,6,1]
def q(l):
    if len(l)<1:
        return l
    else:
        pivot = l.pop()
    l_arm=[]
    r_arm=[]
    for ch in l:
        if ch>pivot and ch not in r_arm:
            r_arm.append(ch)
        elif ch<pivot and ch not in l_arm:
            l_arm.append(ch)
        else:
            print('empty list')
    return q(l_arm)+[pivot]+q(r_arm)
print(q(lt))


