print("Zadanie 1")
n=6
tab = [0,1]
for i in range(2,n+1):
    tab.append(tab[-1] + tab[-2])
print(tab)

print("Zadanie 2")
suma = 0
for i in tab:
    suma+=i
print(suma, end=" ")
print("LUB", sum(tab))

print("Zadanie 3")
sumap = 0
for i in tab:
    sumap+=i if i%2==0 else 0
print(sumap)

print("Zadanie 4")
T = []
for i in range(n+1):
    T.append(i*2 if i%2==0 else i-1)
print(T)

print("Zadanie 5")
factorial = 1;
for i in range(1,n+1):
    factorial*=i
print(factorial)

print("Zadanie 6")
maxv = 0
for i in range(n+1):
    maxv = T[i] if maxv<T[i] else maxv
print(maxv, end=" ")
print("LUB", max(T))

print("Zadanie 7")
maxi = 0
for i in range(n+1):
    #print(maxi, i, maxv, T[i])
    maxi = i if maxv==T[i] else maxi
print(maxi)

          
