from random import randint, choice
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
N = 10000
a = []
for i in range(N):
    a.append(randint(1, 9999))
print(a)