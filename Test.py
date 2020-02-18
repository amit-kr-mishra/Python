nums =[2,4,8,5,6]
target=7
dict= {}
for i in range(len(nums)):
    print("hello ", nums[i])
    if nums[i] in dict:
        print(dict[nums[i]],i)
    else:
        dict[target-nums[i]]= i
print("-----------------")
print(dict)
