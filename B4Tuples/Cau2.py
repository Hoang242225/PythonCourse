Mydict = {
        "Name":"Ten",
        "Age" :["Tuoi","Thoi ki"],
        "School":"Truong",
        "Class":["Lop", "Phan loai"],
        "ID"   :"Ma dinh danh"
        }
print(Mydict)
print(len(Mydict))
Mydict["KTRB"] = "Ky thuat Robot"
print(Mydict)

def Dict_SearchingKey(key, Dict):
    if key in Dict:
        print('{} from {}'.format(Dict[key], key))
    else:
        print('Can not find this word!!!')
    return 0;

Dict_SearchingKey("Age", Mydict)


def Dict_SearchingValue(val,Dict):
    for key, value in Dict.items():
        if val == value:
            print(key)

print("Search 'Truong' : \n")
Dict_SearchingValue("Truong", Mydict)

def Del_Key(key, Dict):
    if key in Dict:
        del Dict[key]
        print(Dict)
    else:
        print("Tu khong ton tai")

Del_Key("Name", Mydict)

