'''base functions to practice string operations'''
'''Most of them are solution to CodingBat problems from https://codingbat.com/python'''

def format_string():
    print('Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \t\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are')
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if(negative):
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b >0) or (b < 0 and a >0))

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. \n The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    return (str[0:n] + str[n+1:len(str)])

# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if(len(str) <= 1):
        return str
    else:
        new_str = str[len(str)-1] + str[1:len(str)-1] + str[0]
    return new_str

# Just spelling words backwards
def spell_backwards(str):
    return str[::-1]

# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  if(len(str) <= 1):
    return str
  else:
    new_str = str[0]
    for i in range(1,len(str)):
      if(i%2 == 0):
        new_str+=str[i]
    return new_str

def string_splosion(str):
  new_str = ''
  for i in range(len(str)):
    if(len(str) == 1):
      return str
    if(i == 0):
        new_str += str[i]*2
    elif (i == 1):
        new_str += str[i]
    else:
        new_str += str[0:i+1]
  return new_str

'''Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).'''
def last2(str):
    substring = str[len(str) - 2: len(str) ]
    firststring = str[:len(str)-2]
    count = 0
    for i in range (len(firststring)):
        new_substr = str[i: i+2]
        if(new_substr == substring):
            count += 1
    return count

'''Given an array of ints, return the number of 9's in the array.'''

def array_count9(nums):
  count9 = 0
  for i in range(len(nums)):
    if(nums[i] == 9):
      count9 += 1
  return count9

'''Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.'''

def array_front9(nums):
  bool = False
  for i in range(len(nums[:4])):
    if(nums[i] == 9):
      bool = True
  return bool

'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''

def array123(nums):
  bool = None
  if(len(nums)<3):
      return False
  for i in range(len(nums)-1):
    if(nums[i] == 1):
        if(nums[i+1] == 2):
            if(nums[i+2] == 3):
                bool = True
  if bool is None:
      bool = False
  return bool

'''Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
'''
def string_match(a, b):
    matches = 0
    for i in range(len(a) - 1):
        substr_a = a[i] + a[i+1]
        if i == len(b)-1:
            break
        else:
            substr_b = b[i] + b[i+1]
        if substr_a == substr_b:
            matches += 1
    return matches

'''Given an array of ints length , return a new array with the elements in reverse order'''
def reverse3(nums):
  new_array=[]
  for i in reversed(range(0, len(nums))):
    new_array.append(nums[i])
  return new_array

'''Given an array of ints, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

'''
def max_end3(nums):
  new_array=[]
  if(nums[0] >= nums[len(nums)-1]):
    higher_number = nums[0]
  else:
    higher_number = nums[len(nums)-1]
  for i in range(0,len(nums)):
    new_array.append(higher_number)
  return new_array

'''Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

'''

def sum2(nums):
  count = 0
  if (len(nums) == 1):
    count += nums[0]
  elif(len(nums)>1):
    for i in range(2):
      count += nums[i]
  return count

'''Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

'''
def middle_way(a, b):
  new_array = []
  middle_point_a = len(a)/2
  middle_point_b = len(b)/2
  new_array.append(a[middle_point_a])
  new_array.append(b[middle_point_b])
  return new_array

'''Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

'''

def make_ends(nums):
  new_array = []
  if (len(nums) <=1):
    new_array.append(nums[0])
    new_array.append(nums[0])
  else:
    new_array.append(nums[0])
    new_array.append(nums[len(nums)-1])
  return new_array

'''Given an int array length 2, return True if it contains a 2 or a 3.

'''

def has23(nums):
  pos1 = nums[0]
  pos2 = nums[1]
  return pos1 == 2 or pos2==3 or pos1==3 or pos2==2

'''Given a string, return a string where for every char in the original, there are two chars.

'''
def double_char(str):
  new_str = ""
  for i in str:
    new_str += 2*i
  return new_str

'''Return the number of times that the string "hi" appears anywhere in the given string.

'''
def count_hi(str):
  hi_times = 0
  for i in range(len(str) - 1):
    if(str[i]+str[i+1] == 'hi'):
      hi_times += 1
  return hi_times


'''Return True if the string "cat" and "dog" appear the same number of times in the given string.

'''
def cat_dog(str):
  cat_sum = 0
  dog_sum = 0
  for i in range(len(str)):
    if(str[i:i+3] == 'cat'):
      cat_sum +=1
    if(str[i:i+3] == 'dog'):
      dog_sum +=1
  return cat_sum == dog_sum

'''Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

'''

def count_code(str):
  code_count = 0
  for i in range(len(str)-3):
    if(str[i:i+2] == 'co' and str[i+3] == 'e'):
      code_count += 1
  return code_count

'''Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences'''
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b[len(b)- len(a): len(b)] == a) or (a[len(a)- len(b):len(a)] == b)


'''Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

'''
def xyz_there(str):
    for i in range(len(str)):
        if (str[i:i+3] == 'xyz' and str[i-1] != '.'):
            return True
    return False

'''Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.'''

def spell_backwards_names():
    name = input('Podaj swoje imię')
    surname = input('Podaj swoje nazwisko')
    fullname = spell_backwards(name)+ " "+spell_backwards(surname)
    return fullname

'''Write a Python program to accept a filename from the user and print the extension of that.'''

def print_extension():
    get_filename = input("Podaj nazwę pliku: ")
    extension = get_filename.split(".")
    return extension[-1]
