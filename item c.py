import math
from collections import defaultdict

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
epsilon = b-a

Q = math.ceil(1/epsilon)

def key(x):
    keys = [(Q-i-1)/Q for i in range(Q)]
    for k in keys:
        if x*math.pi%1 >= k: return k
        
def partition():
    interval = defaultdict(list)
    for n in range(Q+1): interval[key(n)].append(n)
    
    return interval

S1 = partition()
for subinterval in S1.values():
    if len(subinterval)>=2: k = subinterval[1]-subinterval[0]

j=0
Pj=0
while abs(Pj-a%1)>=(b-a)%1 or abs(Pj-b%1)>=(b-a)%1:
    j+=1
    Pj = j*k*math.pi%1
    
print(f'n = {j*k}')
print(f'nα = {j*k*math.pi}')