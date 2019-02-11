list=[]
num=int(input())
m=int(input())
k=0
for n in range(num):
    numbers=int(input())
    list.append(numbers)
for i in range(m):
    k=k+list[i]
print(k)
