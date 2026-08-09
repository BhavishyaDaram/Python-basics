#traversing through dictionary
# d={10:100,20:200,30:300,40:400}
# for i in d:
#     print(i)

#Write a code to sum a dictionary
# d={10:100,20:200,30:300,40:400}
# sum=0;
# for i in d:
#     sum+=d[i]

# print(sum)

#count frequency of each element
# a=[1,1,1,2,2,2,3,3,4,4,4,5,5,6,7,8]

# d={}
# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i]=1
# print(d)
#combine two dicts
d1={10:100,20:200,40:300}
d2={40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)









