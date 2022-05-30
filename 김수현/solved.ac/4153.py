while True: 
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    h = max(nums)
    nums.remove(h)
    if nums[0]**2 + nums[1]**2 == h**2:
        print("right")
    else:
        print("wrong")