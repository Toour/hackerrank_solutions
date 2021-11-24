x = int(input())
y = int(input())
z = int(input())
n = int(input())
array = []

for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if (a+b+c) != n:
                lil_list = [a,b,c]
                array.append(lil_list)
print(array)
