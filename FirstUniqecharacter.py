from collections import Counter
s="LeetcodecoLt"
dict ={}
#i = 0

#char_counts = Counter(s)
def uniqueChar(s):
    #print(char_counts)
    for i  in range(len(s)):
        if s[i] in dict:
            dict[s[i]]=-1
        else:
            dict[s[i]]= i

    #for j in range(len(s)):
    for key,val in dict.items():
        if val != -1 :
        # if j in dict.values():
             print("First Unique Char position is :", key )
             return key
            # print(s[j])
         #else :
             #j+=1

print(dict)
print(uniqueChar(s))
