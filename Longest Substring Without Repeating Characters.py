Input = "Pabcabcd"
dict={}
n = len(Input);
i =  minIndex =  maxLength = 0
while (i < n):
    if  Input[i] in dict:
        minIndex = max(minIndex, dict[Input[i]] + 1)
    dict[Input[i]] = i;
    i += 1;
    maxLength = max(maxLength, i - minIndex)

print(dict)
print(" Length of the Substring is :", maxLength)
