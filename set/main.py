# # #Creating  a Set:
#
# Myset = {"apple", "banana", "cherry"}
# print(Myset)



# # #Duplicate values will be ignored:
#
# Fruits = {"apple", "dragonfruit", "cherry", "apple", "strawberry"}
#
# print(Fruits)



# # #Check length Getting the number of items in a set:
#
# Myfav = {"doraemon", " nobita","sunio" , "shizuka"}
#
# print(len(Myfav))

#printing 2 sets togethere
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# #note gives unorderd ans
# print(set1.union(set2))

# #printing symmetric differance
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))

# set operations
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# if set1.isdisjoint(set2):
#   print("Two sets have no items in common")
# else:
#   print("Two sets have items in common")
#   print(set1.intersection(set2))