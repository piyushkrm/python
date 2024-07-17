# set are not accessing by index value
se = {1, 2, 5, 2, 8, 3, 114, 568, 110, 897, 6, 6, 5, "PIHU", "PIHU", "PIHU", "piyush"}
se.add("sona")                             # add element
print(se)

se.remove(2)                                   # remove element if elemet are not present then through an key error
print(se)

se.discard(0)                           # remove element Nothing if element are not present
print(se)

se.pop()                                            # remove rendom element from the set if not present in the set then through an error
print(se)

se1 ={ "piyush", "mishra", "palak", "aayush", "abhinav", "harsh", "prasun", "daisy"}
setUnion = se1.union(se)
print(setUnion)                                 # add two set together

setIntersection = se1.intersection(se)
print(setIntersection)                      # return common element from the set


set0 = {1, 2, 3, 4, 5}
set9 = {0, 9, 8, 7, 6, 5}

set0.update(set9)                                  # update the set
print(set0)
print(len(set0))                           # length of an set


print(set0.issubset(set9))