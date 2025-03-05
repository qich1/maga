kol=0
min=10**10
f=open('C:/programs/17-1.txt')
s=f.read().split()
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(len(s)-1):
    if s[i+1]>s[i]:
        raz=abs(s[i]-s[i+1])
        kol=kol+1
        if raz<min:
            min=raz
print(kol,min)