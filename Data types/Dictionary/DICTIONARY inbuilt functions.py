# DICTIONARY INBUILT FUNCTIONS
a={"id":"ragu","mental helth":"ok","id num":7}
for i in a.keys():
    print(i)
for j in a.values():
    print(j)
for k in a:
    print(k)

if "id" in a:
    print("prsent")

# DICTIONARY INBUILT FUNCTIONS
b={}
b.update(a)
print(a)
b.pop("id num")
print(b)
b.clear()
print(b)
