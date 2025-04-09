def prevsmallerele(nums):
    n = len (nums)
    st = []
    pse = []

    for i in range(n):
        while len(st) > 0 and st[-1] >= nums[i]:
            st.pop()
        
        if len(st) == 0:
            pse[i] = -1
        else:
            pse[i] = st[-1]

        st.append(nums[i%n])
    return pse