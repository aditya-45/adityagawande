a,b = map(int,input().split())
l = []
for i in range(a):
        l.append(input())
num1 = 0
num2 = 0
st = ""
s = ""
for i in range(len(l)):
    if "*" in l[i] and l[i].count("*")==1:
        s = l[i]
        num1 = i+1
    if l[i].count("*")==2:
        st = l[i]
        num2 = i+1
g = 0
h = 0
x = 0
for i in range(len(s)):
    if s[i]=="*":
        x  = i+1
for i in range(len(st)):
    if st[i]=="*":
        if g==0:
            g = i+1
        elif h==0:
            h = i+1
if g==x:
    print(num1,h)
elif h==x:
    print(num1,g)
