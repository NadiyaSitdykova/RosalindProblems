def mortal_fibonacci(n, m):
    total = [1]
    newborns = [1]
    for i in range(1, n):
        adult = total[i-1] - newborns[i-1]
        newborns.append(adult)
        alive = total[i-1]
        if i >= m:
            alive -= newborns[i-m]
        total.append(alive + newborns[i])
    return total[n-1]

with open("input.txt", 'r') as file:
    n, m = map(int, file.readline().split())

with open("output.txt", 'w') as out:
    out.write(str(mortal_fibonacci(n, m)))