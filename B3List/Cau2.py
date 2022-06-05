mylist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(mylist[0:2])
print(mylist[-2:])
def del_fale(mylist): 
    del mylist[0]
    del mylist[-1]

del_fale(mylist)
print(mylist)
