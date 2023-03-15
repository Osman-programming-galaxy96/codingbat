'''
Return the number of even ints in the given array.'''


def count_evens(nums):
    even_counter = 0
    for i in nums:
        if i % 2 == 0:
            even_counter += 1
    return even_counter

'''Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.'''


def big_diff(nums):
    min_val = min(nums)
    max_val = max(nums)
    return max_val - min_val

'''Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

'''
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


def centered_average(nums):
    new_array = []
    counter = 0
    for i in nums:
        if (i != min(nums) and i != max(nums)):
            new_array.append(i)
            counter += i
    if (counter > 0):
        return counter // len(new_array)
    return counter
'''Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

'''
def sum13(nums):
    pos13 = 0
    print('pos', len(nums))
    for j in range(0, len(nums)):
        if nums[j] == 13:
            pos13 = j
            return sum(nums[:j])
    return sum(nums)

'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

'''


def sum67(nums):
    sum_nums = 0
    isBetween = False
    for i in range(len(nums)):
        if nums[i] == 6:
            isBetween = True
        if not isBetween:
            sum_nums += nums[i]
        if nums[i] == 7 and isBetween:
            isBetween = False

    return sum_nums

'''Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

'''
def has22(nums):
  has2Near = False
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      has2Near = True
  return has2Near

