from itertools import permutations
test = 0,1,2,3,4,5,6,7,8,9
test1 = 0,1,2
permuteCount = 0
for i in permutations(test):
    permuteCount += 1
    if permuteCount == 1000000:
        print("Permutation number 1000000 is ",i)
print("The number of possible permutations is",permuteCount)
