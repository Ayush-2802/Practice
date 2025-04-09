def nextGreaterElements(nums):
    # n = len(nums)
    # nge = [-1]*n

    # for i in range(n):
    #     for j in range(i+1,i+n):
    #         ind = j % n
    #         if nums[ind] > nums[i]:
    #             nge[i] = nums[ind]
    #             break
        
    # return nge
            
    n = len(nums)
    st = []
    nge = [-1]*n

    for i in range(2*n-1,-1,-1):
        while len(st) > 0 and st[-1] <= nums[i%n]:
            st.pop()

        if i < n:
            if len(st) == 0:
                nge[i] = -1
            else:
                nge[i] = st[-1]
            
        st.append(nums[i%n])

    return nge