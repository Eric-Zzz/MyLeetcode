# Given a binary array, find the maximum number of consecutive 1s in this array.



class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        find = 0
        L=[i for i, v in enumerate(nums) if v == find]
        if len(L)==1:
            res1=L[0]
            res2=len(nums)-L[0]-1
            if res1>=res2:
                return res1
            else:
                return res2
        elif len(L)==0:
            return len(nums)
        else:
            res=L[1]-L[0]
            res3=len(nums)-L[-1]
            for i in range(len(L)-1):
                sum1=L[i+1]-L[i]
                if sum1>=res:
                    res=sum1
            if res>=res3:
                return res-1
            else:
                return res3-1

