d=int(input())
n=int(input())
lis=[[0 for i in range(129)]for j in range(129)]
num=0
maxi=0
l1=[0]
for i in range(0,n):
    x,y,k=map(int,input().split())
    lis[x][y]=k
    for g in range(x-d,x+d+1):
        for h in range(y-d,y+d+1)
                    maxi=maxi+lis[g][h]
            if maxi>l1[0]:
                l1.pop()
                l1.append(maxi)
                num=1
            elif maxi==l1[0]:
                num=num+1
                maxi=0
            elif maxi<l1[0]:
                num=num
                maxi=0
print(num,' ',l1[0])
                    













