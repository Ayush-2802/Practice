class BS:
    def rec(self,nums,target,low,high):
        if low> high: return -1
        mid = low + (high-low)//2 #overflow prevention
        if nums[mid] == target: return mid
        elif target > nums[mid]: return self.rec(nums,target,low,mid-1)
        else: return self.res(nums,target,mid+1,high)

    def bs(self,nums,target):
        return self.rec(nums,target,0,len(nums)-1)