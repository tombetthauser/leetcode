class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # nums can be negative
        # shoot for better than O(n^2) time
        
        # nested iteration over all num pairs
          # return indices when target is found
          # this is O(n^2)
          
        # use a hashmap?
        # iterate over nums
        # log num and index in hashmap --> num as key and index as val
        # determine complement num needed to reach the target with current num
          # ie target_num: 10 --> current_num: 4 --> compliment_num: 6
          # if compliment has been logged
            # return indices of each
              # current_idx and logged_num_indices[compliment_num]
              
        # edge case? [5,1,2] with target = 10 <-- not covered
              
        num_indices = {}
        
        for idx, current_num in enumerate(nums):
          compliment_num = target - current_num
          if compliment_num in num_indices:
            return [idx, num_indices[compliment_num]]
          num_indices[current_num] = idx
          
        # O(n) time | O(n) space
        
    def twoSum2(self, nums, target):
        # We can do better with space
        # sort the input array in place
        # store original indices by replacing elements with tuples
          # ie [(sorted_num, original_index), ...]
        # then we could use pointers to start at sorted ends
        # checking the sum of each pair
        # if it's lower than target moving the left right
        # if it's higher than target moving right left
        # we'd have to write a custom sort callback to work with tuples
        # O(nlogn) would still be our time but we'll have O(1) space back
        
        # get tuples
        # define sort callback
        # sort tuples
        # make pointers
        # while left < right
          # get sum
          # if sum is target return indices
          # if sum < target left++
          # if sum > target right--
          
        
        nums = [(idx, num) for (idx, num) in enumerate(nums)]
        
        def sort_cb(a, b):
          if a[1] > b[1]:
            return 1
          if a[1] == b[1]:
            return 0
          else:
            return -1
          
        nums.sort(sort_cb)
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
          left_tup = nums[left]
          right_tup = nums[right]
          curr_sum = left_tup[1] + right_tup[1]
          if curr_sum == target:
            return [left_tup[0], right_tup[0]]
          elif curr_sum < target:
            left = left + 1
          else:
            right = right - 1