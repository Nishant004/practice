height = [1,8,6,2,5,4,8,3,8,7]
# height = [1,1]

left=0
right=len(height)-1
achight=0
 
maxarea=0

while left < right:
    achight=min(height[left],height[right])
    if achight == height[left]:
        maxarea = max(maxarea, ((right - left) * achight))
        left +=1
    else:
        maxarea = max(maxarea, ((right - left) * achight))
        right -=1
print(maxarea)
