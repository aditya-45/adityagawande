a,b = map(int,input().split())
count = a
i = 1
g = b
while(b<=a):
    b = g*i
    if(b<=a):
        count += 1
    else:
        break
    i += 1
while(g*i<=count):
    if g*i<=count:
        count += 1
    i += 1
print(count)
