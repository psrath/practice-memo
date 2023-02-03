s='xbcdabcd'
if len(s)%2 == 0:
    if s[:len(s)//2:]==s[len(s)//2::]:
        print('sym')
    else:
        print('not sym')
else:
    if s[:len(s)//2]==s[len(s)//2+1::]:
        print('sym')
    else:
        print('Not')