def Minimum(number):
    Min = value[0]["Score"]
    for index1 in range(len(number)):
        if value[index1]["Score"] < Min:
            Min = value[index1]["Score"]
    return Min

def Maximum(number):
    Max = value[0]["Score"]
    for index2 in range(len(value)):
        if value[index2]["Score"] > Max:
            Max = value[index2]["Score"]
    return Max

value = [
    {
        "Name":"chum","Score": 20
    },
    {
        "Name":"Vann","Score":300
    },
    {
        "Name":"Socheat","Score": 1
    },
    {
        "Name":"Chet","Score": 120
    }
]
addDic = {}
addDic["The minimum fo the number is"] = Minimum(value)
addDic["The maximum fo the number is"] = Maximum(value)
print(addDic)