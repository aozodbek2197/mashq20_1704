# 1-mashq
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False]*(len(s)+1)
    dp[0] = True
    
    for i in range(1,len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[-1]
# 2-mashq
def decode(s):
    dp = {len(s):1}
    
    for i in range(len(s)-1,-1,-1):
        if s[i]=="0":
            dp[i]=0
        else:
            dp[i]=dp[i+1]
            if i+1<len(s) and int(s[i:i+2])<=26:
                dp[i]+=dp.get(i+2,0)
    
    return dp[0]
# 3-mashq
def largestRectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)
    
    for i,h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i-stack[-1]-1
            max_area = max(max_area, height*width)
        stack.append(i)
    
    return max_area
# 4-mashq
def trap(height):
    l,r = 0,len(height)-1
    left_max = right_max = 0
    res = 0
    
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            res += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            res += right_max - height[r]
            r -= 1
    
    return res
# 5-mashq
def findMedian(a,b):
    nums = sorted(a+b)
    n = len(nums)
    if n%2:
        return nums[n//2]
    return (nums[n//2-1]+nums[n//2])/2
