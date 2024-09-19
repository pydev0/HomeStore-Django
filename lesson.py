my_set = set()
        i = 0

        while not nums:
            if nums[i] not in my_set:
                my_set.append(nums[i])
                i += 1
            else:
                nums.remove(nums[i])
                i += 1
        return nums
