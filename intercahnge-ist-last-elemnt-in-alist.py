lst = [1,2,3,4,5]
def swapElmentList(pos1,pos2,list):
    try:
        lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
    except Exception as e:
        print(f' {e}')
        print('Pls check argument type correctly')
        print(f'u hv given arg1={pos1} and arg2={pos2}')
    return list
#lst[0],lst[-1]=lst[-1],lst[0]
#get = (lst[0],lst[-1])
#lst[-1],lst[0]=get
#print(type(get))
start,*middle,end= lst
start,*middle,end=lst
#lst = [end,*middle,start]
print(lst)
print(swapElmentList('a','b',[]))