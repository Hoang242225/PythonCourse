myList = ["FPGA", "TKCCD", "PBL3", "A", "B", "C"]
newList= ["BK","BOY", "75"]
print(myList)
myList.append("Hoang")
print(f" result after append list {myList}")
myList.insert(2,"Dog")
print(f"result after insert list {myList}")
myList.extend(newList)
print(f"result after extend list {myList}")
print(f"The index of FPGA in the list is:", myList.index("FPGA"))
myList.remove("TKCCD")
print(f"result after remove TKCCS:{myList}")
myList.sort()
print(f"sort the list:{myList}")
myList.reverse()
print(f"reverse the list: {myList}")
myList.pop(2)
print(f"delete the second element in the list: {myList}")
        

