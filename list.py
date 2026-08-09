# largest number in an list
# l=[12,23,43,29,89,33,45]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest = l[i]
#         index=i
# print(f"your largest number is {largest} at index {index}")
#print largest and second largest
# l=[12,23,43,29,89,33,45]
# sec_largest=l[0]
# largest=l[0]
# for i in range(len(l)):
#     if l[i]>largest:
#         sec_largest=largest
#         largest = l[i]
#     elif l[i]>sec_largest:
#         sec_largest=l[i]


# print(sec_largest,largest)
# check if list is sorted or not
l=[12,23,43,89]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("not sorted")
        break
else:
    print("sorted")


