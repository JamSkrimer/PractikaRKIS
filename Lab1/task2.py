nums = [10, 1, 2, 7, 6, 1, 5]
target = int(input())

def find(nums, target, start=0, summa=0, comb=None):
    if comb is None:
        nums.sort()
        comb = []
    if summa == target:
        return [comb[:]]
    result = []
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        if summa + nums[i] > target:
            break
        new = find(
            nums,
            target,
            i + 1,
            summa + nums[i],
            comb + [nums[i]]
        )
        result.extend(new)
    return result

print(f"Числа: {nums}")
print(f"Цель: {target}")
print(f"Результат: {find(nums, target)}")
