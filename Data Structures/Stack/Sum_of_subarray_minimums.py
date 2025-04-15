class Solution:
    def nse(self, arr):
        n = len(arr)
        nse = [n] * n
        st = []

        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                nse[i] = n
            else:
                nse[i] = st[-1]
            st.append(i)
        return nse
    
    def pse(self, arr):
        n = len(arr)
        pse = [-1] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if not st:
                pse[i] = -1
            else:
                pse[i] = st[-1]
            st.append(i)

        return pse
        
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        nse = self.nse(arr)
        pse = self.pse(arr)
        total = 0

        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            
            # Add contribution of this element to all subarrays
            total = (total + arr[i] * left * right) % MOD
        
        return total