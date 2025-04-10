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


def trap(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    leftMax = height[left]
    rightMax = height[right]
    total = 0
    
    while left < right:
        if height[left] < height[right]:
            # Process from left side
            if height[left] >= leftMax:
                # Update left max
                leftMax = height[left]
            else:
                # Add trapped water
                total += leftMax - height[left]
            left += 1
        else:
            # Process from right side
            if height[right] >= rightMax:
                # Update right max
                rightMax = height[right]
            else:
                # Add trapped water
                total += rightMax - height[right]
            right -= 1
    
    return total

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        leftmax = height[l]
        rightmax = height[r]

        total = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    total += leftmax - height[l]
                leftmax += 1
            else:
                if height[r] >= rightmax:
                    rightmax = height[r]
                else:
                    total += rightmax - height[r]
                rightmax -= 1
        
        return total