def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False 

n1 = int(input())
li1 = sorted(map(int, input().split())) 
n2 = int(input())
li2 = list(map(int, input().split()))

result = []
for num in li2:
    if binary_search(li1, num):
        result.append(1)
    else:
        result.append(0)

print(*result)
