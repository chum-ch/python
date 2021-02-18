name = [
    ["Ronan", "Ogor", 2],
    ["Jonathan", "Faucher", 90],
    ["chum", "yoeurn", 3],
    ["vann", "neom", 18]

]

for index in range(len(name)):
    if name[index][2] >= 18:
        name[index].append("Major")
    else:
        name[index].append("Minor")
print(name)
