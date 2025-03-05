kol=0
max=0
f=open('C:/programs/17-1.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(1,len(s)-1):
    if s[i-1]>s[i]<s[i+1]:
        kol=kol+1
        if max<s[i]:
            max=s[i]
print(kol, max)