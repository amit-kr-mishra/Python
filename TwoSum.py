#If Value required from List  then below is fine  but if position is required the it will not work
nums =[2,4,8,5,6]
target = 7

def twoSum(self, nums: List[int], target: int):
    if len(nums)<=1:
        return -1
    dict= {}
    for i in range (len(nums)):
        if nums[i] in dict:
            return dict[nums[i]]
        else:
            dict[target-nums[i]]= i 




print(Two_Sum(A,target))
