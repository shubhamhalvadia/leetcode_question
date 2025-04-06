def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:  # If we find a pair
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:  # If the sum is too small, move the left pointer
                left += 1
            else:  # If the sum is too large, move the right pointer
                right -= 1
        
        return count