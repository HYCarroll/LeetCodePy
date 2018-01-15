//Given an array of integers, return indices of the two numbers such that they add up to a specific target.

//You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i
            else:
                return map[num[i]], i

        return -1, -1
