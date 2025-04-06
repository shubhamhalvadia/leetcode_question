def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[pointer] == 0:
                del nums[pointer]
                nums.append(0)
                pointer -= 1
                # print(nums, i, pointer) 
            pointer += 1