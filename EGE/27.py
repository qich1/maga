kol=0
max=0
arf=0
sum=0


f=open('17-1.txt')
s=f.read().split()

for i in range(len(s)):
    s[i]=int(s[i])

for i in range(len(s)):
    sum = sum+s[i]
    arf = sum/ len(s)

for i in range(len(s)-2):
    if (s[i]<arf or s[i+1]<arf or s[i+2]<arf) and (s[i]%3==0 or s[i+1]%3==0 or s[i+2]%3==0):
        kol=kol+1
        sum=s[i]+s[i+1]+s[i+2]
        if sum>max:
            max=sum
print(kol,max)