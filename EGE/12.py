f=open("C:/programs/17-8.txt")
s=f.read().split()
kol=0
sum=0
max=-10**10
for i in range(len(s)):
    s[i] = int(s[i])
for i in range(len(s)-1):
    sum=s[i]+s[i+1]
    t=s[i]
    sum2=0
    while t>0:
        sum2=sum2+t%2
        t=t//2
    t=s[i+1]
    sum3=0
    while t>0:
        sum3=sum3+t%2
        t=t//2
    if (sum2>5 and sum%2!=0) or (sum3>5 and sum3%2!=0):
        kol=kol+1
        if sum>max:
            max=sum
print(kol,max)



