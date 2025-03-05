kol=0
max=0
fos=0
f=open('C:/programs/17-2.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)):
    if max<s[i]:
        max=s[i]
        fos = i + 1
for i in range(len(s)-1):
    if s[i]==max:
        kol=kol+1
print(kol, fos)