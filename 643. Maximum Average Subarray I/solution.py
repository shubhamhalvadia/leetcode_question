def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        total = sum(nums[:k])
        max_avg = float(total/k)
        if len(nums) < k:
            return 0

        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[k + i]
            curr_avg = float(total/k)
            if curr_avg > max_avg:
                max_avg = curr_avg
        
        return max_avg