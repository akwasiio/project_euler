"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutattion
of the digits 1,2,3,4. If all of the permutations are listed numerically or alphabetically, we call
it lexicographic order. The lexicographic permutations of 0,1 and 2 are:
012,021,102,120,201,210"""

from itertools import permutations
test = 0,1,2,3,4,5,6,7,8,9
test1 = 0,1,2
permuteCount = 0
for i in permutations(test):
    permuteCount += 1
    if permuteCount == 1000000:
        print("Permutation number 1000000 is ",i)
print("The number of possible permutations is",permuteCount)
