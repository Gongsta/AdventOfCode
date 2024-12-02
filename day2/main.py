total = 0


def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1] or arr[i + 1] - arr[i] < 1 or arr[i + 1] - arr[i] > 3:
            return False
    return True


def is_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1] or arr[i] - arr[i + 1] < 1 or arr[i] - arr[i + 1] > 3:
            return False
    return True


for line in open("input.txt"):
    l = line.split()
    l = [int(x) for x in l]
    for i in range(len(l) + 1):
        if is_increasing(l[:i] + l[i + 1 :]) or is_decreasing(l[:i] + l[i + 1 :]):
            total += 1
            break

print(total)
