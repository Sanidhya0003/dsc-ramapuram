mylist=[2,3,4,6,7,7]

result=[]
for i in mylist:
    if i not in result:
        result.append(i)

print(result)
