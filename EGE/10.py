kol=0
max=0
sum=0
f=open('C:/programs/17-5.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)-1):
    if abs(s[i])%10==7 or abs(s[i+1])%10==7:
        sum=s[i+1]+s[i]
        kol=kol+1
        if sum>max:
            max=sum
print(kol,max)