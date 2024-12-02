prev = None
total = 0

a = []
b = []

a_count = {}
for line in open("input.txt"):
    x = line.split()
    a.append(int(x[0]))
    a_count[int(x[1])] = a_count.get(int(x[1]), 0) + 1

a.sort()
b.sort()
total = 0
for val in a:
    total += val * a_count.get(val, 0)

print(total)
