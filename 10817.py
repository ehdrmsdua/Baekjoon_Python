numbers = list(map(int, input().split()))
numbers.remove(max(numbers))
print(int(max(numbers)))
