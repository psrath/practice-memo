#input [1,3,4]
#Output Last number add remaing element will be same
#[1,3,5]

arr = [3,4,1]
if arr[-1]==9 and arr[-2]!=9:
    arr[0],arr[1],arr[2]=arr[0],arr[1]+1,0
elif arr[0]==9 and arr[1] == 9 and arr[2]==9:
    arr[0],arr[1],arr[2]=0,0,0
    arr.append(1)
    arr = arr[::-1]
elif arr[-1]==9and arr[-2]==9:
    arr[0],arr[1],arr[2]=arr[0]+1,0,0
else:
    arr[0],arr[1],arr[2]=arr[0],arr[1],arr[2]+1

print(arr)


