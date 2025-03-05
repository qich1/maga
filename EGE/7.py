kol=0
min=10*10
arf=0
f=open('C:/programs/17-3.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)-1):
    arf=(s[i]+s[i+1])//2
    if s[i]*s[i+1]%2!=0 and arf%7==0:
        kol=kol+1
        if min>arf:
            min=arf
print(kol,min)