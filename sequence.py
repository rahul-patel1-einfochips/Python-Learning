# List -> []
# lst = list([1, 2, 3, 4, 5])
# print("Cretaing list using list() class: ", lst)

# lst = [1, True, "Hello", 4.5, ["New", "List"]]
# print("Creating list using []:", lst)

# lst = [4, 5, 6]
# print("Before appending 1: ", lst)
# lst.append(1)
# print("After appending 1: ", lst)

# print("Clearning list")
# lst.clear()
# print(lst)

# lst = [1, 2, 3, 4, 5, 1, 1, 5, 3, 2]
# print(lst)
# print("Count of 1 is: ", lst.count(9))

# copy_list = lst.copy() # copy_list = lst
# print("Copy list: ", copy_list)

# lst1 = [1, 2, 3, 4]
# lst2 = [5, 6, 7, 8]
# lst1.extend(lst2)
# print("LST1 after extending: ", lst1)

# print("Before appending LST1 in LST2")
# print(lst2)
# lst2.append(lst1)
# print("After appending:", lst2)
     # 0, 1, 2, 3, 4  
# lst = ['A', 'B', 'C', 'D', 'E', 'D']
# value = lst.index('D')
# print("Index", value)

# lst.insert(1, 'Z')
# print(lst)

# value = lst.pop()
# print(f"Pop value: {value}")
# print(lst)

# lst.remove('A')
# print(lst)

# lst.reverse()

# print(lst)

# lst.sort(reverse=True)
# print(lst)

# +ve  0, 1, 2, 3, 4, 5
# -ve  -6, -5, -4, -3, -2, -1
# lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# print(lst[5]) # +ve index

# print(lst[-3]) # -ve index

# print(lst[1: 4]) # +ve Slice

# print(lst[-5: -2]) # -ve Slice
# # =============================
# print(lst[0: 3])
# print(lst[:3])

# print(lst[3: 6])
# print(lst[3:])

# [Starting Index: Ending Index: Step=1]

# print(lst[::])


# Tuple -> ()
# tpl = tuple((1, 2, 3, 4, 5))
# print(tpl, type(tpl))
# tpl = (1, 2, 3, 4, 5)
# print(tpl, type(tpl))
# tpl = ('A',)
# print(tpl, type(tpl))

# tpl = (1, 2, 3, 4, 5)
# print(tpl.count(1))
# print(tpl.index(4))
# print(tpl[::2])
# Existing Obj
# print("Existing OBJ::", id(tpl))

# New Object creation for Tuple
# tpl = tpl + (9, 8, 7, 6) 
# tpl += (9, 8, 7, 6)
# print(tpl)
# print("New OBJ::", id(tpl))

# Set -> {}
# st = set({1,2,3,4,5})
# print(st, type(st))
# st1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# st2 = {11, 12, 13}
# print(st1, type(st1))
# st1.update(st2)
# print(st1)
# st1.add(50)
# print(st1)
# print(st1.difference(st2))

# lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(lst, type(lst))

# st = set(lst)
# print(st, type(st))

# lst = list(st)
# print(lst, type(lst))

# st = {1, 2, 3}
# st2 = {4, 1, 6}
# print(st2.difference(st))
# print(st.pop())
# print(st)

# Dictionary -> {}
# dt = dict({"name": "Rahul", "age": 25})
# print(dt, type(dt))
# dt = {
#     "name": "Rahul",
#     "age": 25,
#     "city": "Surat"
# }
# print(dt, type(dt))
# print("NAME::", dt["name"], dt.get("name"))
# # dt.update({"state": "Gujarat"}) # dt["state"] = "Gujarat"
# dt["state"] = "Gujarat"
# print(dt)
# print(dt.values())
# print(dt.keys())
# # print(dt.fromkeys(["1", "2", "3"], ["A","B", "C"]))
# print(dt.items())
# print(dt.popitem())
# print(dt)

person = [
    {"name": "Rahul", "age": 26, "city": "Surat"},
    {"name": "Prisha", "age": 0.3, "city": "Ahmedabad"},
]
person[0]["age"] = 30
print(person[0]["age"])

person = {
    'Rahul': {"name": "Rahul", "age": 26, "cities": ["Surat", "Jaunpur", "Ahmedabad"]},
    'Prisha': {"name": "Prisha", "age": 0.3, "city": "Ahmedabad"}
}
print(person['Rahul']['cities'][2])
