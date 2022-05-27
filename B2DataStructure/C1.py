# CAU 1:

A = 110
B = 262

# In ra phep toan A+B
print(" Result of {} + {} equal {} ".format(A,B,A+B))

# In ra phep toan A-B
print(" Result of {} - {} equal {} ".format(A,B,A-B))

# In ra phep toan AxB
print(" Result of {} x {} equal {} ".format(A,B,A*B))

# In ra cac phep toan chia
print(" Result of {} / {} equal {} ".format(A,B,A/B)) # Chia thuong
print(" Result of {} % {} equal {} ".format(A,B,A%B)) # Chia lay du
print(" Result of {} // {} equal {} ".format(A,B,A//B))# Chia lay nguyen

# CAU 2:

string = "Python programming is the best course to learn"
a = len(string)
print("Do dai cua chuoi:",a)
print("5 ki tu dau tien cua string:", string[:5])
print("10 ki tu cuoi cua string la:", string[-10:])
print("Thay ki tu 'Python' thanh 'DUT':",string.replace("Python","DUT"))
print("'best' nam o vi tri thu:",string.find("best"))
print("Chuoi nay duoc in hoa het dung hay sai? ", string.isupper())
print("Tach chuoi thanh ki tu:")

def split(string):
    return list(string)
print(split(string))
