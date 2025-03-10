
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

#decode string
str = "11[ab]5[t]6[f]"
temp =0
flag=0
tem=''
res =''

for i in str:
    if i.isdigit():
        
        if(temp !=0):
            temp=int(temp) *10 + int(i)
        else:
            # print(i)
            temp=int(i)
    
    else:
        if(i=="["):
            flag = 1
        
        elif(i ==']'):
            
            res =res + (temp *tem)
            tem=''
            temp=0
            flag=0
        else:
            tem=tem+i
        
    
    
print(res)