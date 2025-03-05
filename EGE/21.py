kol=0
max=0
arf=0
sum=0
kol1=0
sum1=0
max1=0
f=open('C:/programs/17-1.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)):
    kol=kol+1
    sum = sum + s[i]
arf = sum/ kol
for i in range(len(s)-1):
    if s[i]>arf or s[i+1]>arf:
        kol1=kol1+1
        sum1=s[i]+s[i+1]
        if sum1 > max:
            max = sum1
print(kol1, max)