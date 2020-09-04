def three_step(current_sum, nums, target):
    if current_sum == target:
        print(nums)
    if sum(nums)+1 <= target:
        three_step(current_sum+1, nums+[1], target)
    if sum(nums)+2 <= target:
        three_step(current_sum+2, nums+[2], target)
    if sum(nums)+3 <= target:
        three_step(current_sum+3, nums+[3], target)


three_step(0, [], 10)
