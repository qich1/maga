kol=0
max=0
sum=0
f=open('C:/programs/17-5.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)-1):
    if s[i]%10==5 and s[i+1]%10==5:
        sum=s[i+1]+s[i]
        kol=kol+1
        if sum>max:
            max=sum
print(kol,max)