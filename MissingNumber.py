nums=[9,6,4,2,3,5,7,0,1]
#expectedsum= len(nums)* (len(nums)+1)/2
#total = sum(nums)
#diff = expectedsum-total
#print("number is " , diff)
####################################

nums=[0]
numset = set(nums)
if len(numset) == 0:
    print(0)

for i in range(0,len(numset)):
    if i not in numset:
        print("missing num:",i)

