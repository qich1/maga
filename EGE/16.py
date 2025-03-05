kol=0
max=0
sum=0
f=open('C:/programs/17-205.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)-1):
    sum=s[i]+s[i+1]
    if (s[i]%7==0 or s[i+1]%7==0) and abs(sum)%100==19:
        sum=s[i+1]+s[i]
        kol=kol+1
        if sum>max:
            max=sum
print(kol,max)