#SET
# A set is an immutable and unoredred . We can't change anything but we can add a value.

a={1,2,241,131,"ragu",True}
print(a)
print(type(a))

for value in a:
    print(value)
# Adding a value
a.add("ragupathi")
print(a)
 
# UPDATING A SET
b={"pradeep",1,2,3,4}
a.update(b)
print(a)

# Set functions
#Union
ragu={1,2,3,4,5}
pathi={5,6,7,8,9,0}
adding=ragu.union(pathi)
print(adding)

# Intersection
print(ragu.intersection(pathi))

# Symmetric difference
print(ragu.symmetric_difference(pathi))

# Disjoint
print(ragu.isdisjoint(pathi))

# suset
print(ragu.issubset(adding))

# Super set
print(adding.issuperset(ragu))

