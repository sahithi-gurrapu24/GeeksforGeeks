class Solution:
    def leaders(self, arr):
        # code here
        leader = []
        n = len(arr)
        right = arr[-1]
        leader.append(right)
        for i in range(n-2,-1,-1):
            if arr[i] >= right:
                right = arr[i]
                leader.append(arr[i])
        leader.sort(reverse = True)
        return leader

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends