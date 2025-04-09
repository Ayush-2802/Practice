def trap(self, height: List[int]) -> int:
    total = 0
    n = len(height)
    
    leftmax = [0]*n
    leftmax[0] = height[0]
    for i in range(1, n):  # Start from 1 instead of 0
        leftmax[i] = max(leftmax[i-1], height[i])

    rightmax = [0]*n
    rightmax[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        rightmax[i] = max(rightmax[i+1], height[i])  # Use max instead of min


    for i in range(len(height)):
        if height[i] < leftmax[i] and height[i] < rightmax[i]:
            total += min(leftmax[i], rightmax[i]) - height[i]
        
    return total