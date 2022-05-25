while True:
    nums = sorted(map(int, input().split()))
    if 0 in nums:
        break

    if nums[-1] ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print('right')
    else:
        print('wrong')