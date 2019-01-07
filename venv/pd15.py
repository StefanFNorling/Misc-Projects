def timeconverter(num):
    return str(num // 60) + ":" + str(num % 60)
print(timeconverter(int(input("Enter a number to put into hours and minutes: "))))

def no_teen_sum(a, b, c):
    teens = [13,14,17,18,19]
    nums = [a,b,c]
    sum = 0
    for num in nums:
        if num not in teens:
            sum += num
    return sum

def lucky_sum(a, b, c):
    nums = [a,b,c]
    sum = 0
    for num in nums:
    if num == 13:
      return sum
    else:
      sum += num
    return sum

def make_bricks(small, big, goal):
    i = 0
    temp = goal
    while i < big and temp >= 0:
      temp = temp - 5
      i += 1
    if temp < 0:
      temp += 5
    if small >= temp:
      return True
    else:
      return False

def round_sum(a, b, c):
  nums= [a,b,c]
  sum = 0
  for num in nums:
    if num % 10 >= 5:
      num = num // 10 * 10 + 10
      sum += num
    else:
      num = num // 10 * 10
      sum += num
  return sum