
a = int(input())
b = int(input())
c = int(a*b)
# print(c)
def fact(a):
    if a == 1:
        return 1
    else:
        return (a *fact(a - 1))



p = fact(c // 2)
c = int(fact(c))
# print(c)
print(p)
# while (k != 0):
#     p *= k
#     k -= 1



# print(p)

c = int((int(c) / int(p*p)))
c = int(c)
# print(c)