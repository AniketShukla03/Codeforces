t = int(input())
for _ in range(t):
    a = int(input())
    count = [1]
    for i in range(2, a,  1):
        
        if i**2 <= a:
            count.append(i**2)
        else:
            break
        if i**3 <= a:
            count.append(i**3)
            
    count = set(count)
    print(len(count))
