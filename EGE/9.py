kol=0
max=0
sum=0
f=open('C:/programs/17-5.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)-1):
    if s[i]%2==0 or s[i+1]%2==0:
        sum=s[i+1]+s[i]
        kol=kol+1
        if sum>max:
            max=sum
print(kol,max)
