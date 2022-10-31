a = int(input())
a1 = a%10
a12 = a//10
b1 = a12%10
b12 = a12//10
c1 = b12%10
c12 = b12//10

b = (b1*10)
a = (a1*100)
c = sum([c1, b, a])
print(c)