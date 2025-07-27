# time complexity O(n^2)
# space complexity O(n)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        #looping for left nums and locking in l 
        for l in range(0, len(nums)):
            #skip and potential duplicates / copies
            if l > 0 and nums[l] == nums[l-1]:
                continue


            #starting pointer for two pointer solution
            r = len(nums) - 1
            i = l + 1
            while (i < r):
                sum = nums[l] + nums[i] + nums[r]
                # since the sum is less than 0 we want to increase 
                # the number so we increment i
                if sum < 0:
                    i += 1
                # since the sum is greater than 0 we want to increase 
                # the number so we increment r
                elif sum > 0:
                    r -= 1
                # found a solutions we will also get rid of duplicates
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    i += 1
                    while nums[i] == nums[i-1] and i < r:
                        i += 1
                
        return res





                        j += 1
        
