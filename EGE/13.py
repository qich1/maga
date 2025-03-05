f=open("C:/programs/17-10.txt")
s=f.read().split()
kol=0
sum=0
min=10**10
edin=0
des=0
for i in range(len(s)):
    s[i] = int(s[i])
for i in range(len(s)-1):
    sum=s[i]+s[i+1]
    des=sum//10%10
    edin=sum%10
    if 99<sum<1000 and edin>des:
        kol=kol+1
        if min>sum:
            min=sum
print(kol, min)
