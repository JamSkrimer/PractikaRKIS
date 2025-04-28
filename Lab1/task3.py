import random
nums = [random.randint(0, 10) for _ in  range(5)]
print(nums)
def dubl(stuff):
    return len(stuff)!=len(set(stuff))

print(dubl(nums))