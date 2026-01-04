"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
Example 1:
Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
"""
#solution:

class Solution:
    def findDivLen(self, num):
        count = 2
        i = 2
        sum_ = 1+num
        if int(math.sqrt(num))**2 == num:
            return 0
        while i<=math.sqrt(num):
            if num%i == 0:
                sum_ = sum_ + i + num/i
                count = count + 2
            if count > 4:
                return 0
            i = i + 18
        if count == 4:
            return sum_
        else:
            return 0
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = self.findDivLen(i)
                ans = ans + hashmap[i]
            else:
                ans = ans + hashmap[i]

        return int(ans)
        