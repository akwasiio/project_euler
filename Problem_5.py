"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without a remainder.


What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def find_smallest_multiple():
    start_point = 2520
    divisors = [v for v in range(11, 21)]
    smallest_multiple = 0

    count = 0
    while True:
        if count == 20:
            smallest_multiple = start_point
            break

        for i in divisors:
            if start_point % i == 0:
                count += 1
            else:
                count = 0
                start_point += 2
                continue

    return smallest_multiple

print(find_smallest_multiple())
print("outside")
