t = int(input())
l = list(input().split())
mid = []
res = []
l = [int(i) for i in l]
for i in range(1, len(l) + 1):
    t = [0] + l[:(i)-1]
    #print(t)
    x = max(t)
    mid.append(x)
print(l)
print(mid)
for i in range(len(l)):
    res.append(l[i]-mid[i])
print(res)
