name = [
    ["Chum","Yoeurn", 10],
    ["Jonathan", "Faucher",25],
    ["Seiha", "Hi", 30],
    ["Ronan","Ogor",15]
]

def add_and_remove(name):
    del name[index][0]
    name[index].insert(0, "Added new name(...)")
    name[index].append("Major")
    return add_and_remove
    
for index in range(len(name)):
    if (name[index][0] == "Chum" or name[index][0]=="Seiha") and (name[index][2] >= 18):
        add_and_remove(name)
print(name)
