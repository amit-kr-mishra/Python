# Genertae Prime number
# 1, 2,3, 5,7, 11

MaxNum , TotalVal = 15,0

for i in range (MaxNum):
     if i > 1:
        for val in range (2, i):
            if i  % val == 0 :
                break
        else:
            print(i)
            TotalVal=  TotalVal + i
print (TotalVal)
