Mytuple = ("Che", "Nam", "Hoang", "mot", "hai", "ba", "bon", "sau", "chin", "muoi")
print(Mytuple)
print(Mytuple[0:10])
print(Mytuple[-9:-1])

def s_find(x,Tuple):
    y = list(Tuple)
    return y.count(x)
y = s_find("Che", Mytuple)
print(y)
