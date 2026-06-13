# #list - ordered, indexed, [], mutable- can change during runtime, heterogenous 
# l=[12,43,'hello',True,4.45,'hi',44]
# print(l)
# print(type(l))

# # slicing 
# # print(l[:])
# # print(l[:4])
# # print(l[1:4])
# # print(l[1:4:1])
# # print(l[1:6:2])
# # print(l[::-1])

# #methods 
# # remove and pop 
# l1=[33,45,22,10,99,87,65]
# print(l1)
# # l1.pop()
# # l1.pop(2)
# # print(l1)
# # Remove and return item at index (default last).
# # Raises IndexError if list is empty or index is out of range.

# # l1.remove(22)
# # print(l1)


# l1.insert(3,100)
# print(l1)
# # print(len(l1))

# # sort 
# # l1.sort()
# # print(l1)

# # append or extend
# l1.append(11)
# # l1.append([12,13,14])
# # print(l1)
# # print(l1[9])
# # print(l1[9][1])
# l1.extend([44,33,21])
# print(l1)

# # for i in l1:
# #     print(i+10)

# j=[]
# for i in range(0,35):
#     if i%7==0:
#         j.append(i)
# print(j)

# # Find all of the words in a list of strings that are less than 4 letters
# n=["karan","Manmeet","Hi","Dog","Cat","Hello"]

# u=[]
# for i in n:
#     if len(i)<4:
#         u.append(i)
# print(u)


# a=[12,13,14,15,16]
# b=[45,55,66,54,45,44]

# for i in zip(a,b):
#     print(i)

# list comprehension 
# l=[]
# for i in range(0,20):
    # if i%2==0:
#       l.append(i)
# print(l)

# l=[i for i in range(0,20)]
# l=[i for i in range(0,20) if i%2==0]
# print(l)

# p=[32,22,10,15,19,20,25,78,100]
# p=[i+2 for i in p]
# print(p)


# p=[i if i%3==0 else i**2 for i in range(1,25)]
# print(p)

# a=[12,13,15,6,7]
# b=[4,5,6,7,10]

# for i in a:
#     for j in b :
#         if i==j:
#             print(i)
# for i in a:
#     if i in b:
#             print(i)

# k=[i for i in a for j in b if i==j]
# k=[(i,i) for i in a if i in b]
# print(k)