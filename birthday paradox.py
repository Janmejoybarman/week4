'''import random
l=[]
l.append(random.random())
l.append(random.random())
l.append(random.random())
print(l)
'''
import random

l = []
flag = 0
for i in range(100):
    l.append(random.randint(1, 365))

l.sort()
print(l)
i = 0
flag = 0
u = []
while (i < len(l) - 1):
    if l[i] == l[i + 1]:
        u.append(l[i])
        flag = 1
    i = i + 1
if flag == 1:
    print('repetation', u)
else:
    print('No repetation')