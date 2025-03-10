
#move zeroes to the end
a=[7,0,4,0,1,0,8,9]


l=0
r=len(a)-1

while(l<r):
    print(l)
    print(r)
    if(a[l] ==0 and a[r]!=0):
        a[l],a[r]=a[r],a[l]
        l=l+1
        r=r-1
        # print('l:')
    else:
        l=l+1
print(a)