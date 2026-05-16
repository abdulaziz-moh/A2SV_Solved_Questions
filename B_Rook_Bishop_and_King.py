r1, c1, r2, c2 = map(int, input().split())
a = 1 if r1 == r2 or c1 == c2 else 2

st1 = 'black' if r1%2 != c1%2 else 'white'
st2 = 'black' if r2%2 != c2%2 else 'white'

if st1 != st2:
    b = 0
else:
    b = 1 if abs(r1-r2) == abs(c1-c2) else 2

c = abs(r1-r2) + abs(c1-c2) - min(abs(r1-r2), abs(c1-c2))
print(a,b,c)