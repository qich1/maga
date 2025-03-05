kol=0
min=10**10
arf=0
sum=0
kol1=0
sum1=0
kol11=0
t=0

f=open('17-4.txt')
s=f.read().split()

for i in range(len(s)):
    s[i]=int(s[i])

for i in range(len(s)):
    sum = sum + s[i]
arf = sum/ len(s)

for i in range(len(s)-1):
    t=s[i]
    d=s[i+1]
    kol7=0
    while t > 0:
        if t % 10 == 7:
            kol7 = kol7 + 1
        t=t//10
    kol72=0
    while d>0:
        if d%10==7:
            kol72=kol72+1
        d=d//10
    if (s[i]<arf or s[i+1]<arf) and (kol7>0 or kol72>0):
        kol11=kol11+1
        sum1=s[i]+s[i+1]
        if min>sum1:
            min=sum1
print(kol11,min)