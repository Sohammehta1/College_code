arr = [1, 2, 3, 4, 5]
target = 8
ans = []

for i in range(len(arr) - 2):
    low, high = i + 1, len(arr) - 1
    while low < high:
        if arr[i] + arr[low] + arr[high] == target:
            ans.append([arr[i], arr[low], arr[high]])
            low += 1  # Move low pointer forward to find the next potential solution
            high -= 1  # Move high pointer backward to find the next potential solution
        elif arr[i] + arr[low] + arr[high] < target:
            low += 1  # If sum is less than target, move low pointer to the right
        else:
            high -= 1  # If sum is greater than target, move high pointer to the left

print(ans)
                 