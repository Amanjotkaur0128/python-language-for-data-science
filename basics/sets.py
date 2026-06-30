# sets - {}
# 1. It is a mutable data type
# 2. Unindexed
# 3. Stores the value in unordered format
# 4. Donot allow the duplicate values
# 5. Defined by {} (curly) brackets
# 6. It can store heterogenous type of data
# 7. takes 0 and false 
# 8. used to remove dublicat values in lists

# a={} # by default it is assigned to the dictionary data structure
# b={15} # it is an set
# d=set() # empty set
# print(type(a))
# print(type(b))
# print(type(d))
# s1= {25,"jatin",52,25,"jatin",}
# print(s1)

# traversing the  sets
# for s in s1:
#     print(s,end=" ")


# Add an element in the set
# s1.add("sumit")
# print(s1)

# Add multiple elements in the set
# s1.update([2,"sonu",45])
# print(s1)

# # Removing the element from the set 
# s1.pop() # it removes the random element from the set(that is present at front)
# print(s1)

# s1.remove(45)# remove an specific item,it must be a member, throw error if item is not present in the set 
# # s1.discard(45) #remove an element from set, dont throw error if item is not present in the set 
# print(s1)

# s1.remove(56)
# s1.discard(56)
# print(s1)

# Common Set Operation 
# union 
# intersection 
# difference 
# symmetric difference

# a={1,2,3,4}
# b={3,4,5,6}
# print(a | b)  # union
# print(a.union(b))
# print(a & b)  # intersection
# print(a -b) # differnce elements that are present only in a
# print(a ^ b) # elements that are not common in both

# print(a.issubset(b))

# f=frozenset({1,2,3,4,5})
# print(f)

# f.add(8)