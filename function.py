from code.armstrong import armstrong
a = 123
print(armstrong(a))

print("------------------------------------------------------------")
print("We are currently inside function.py file")
from code.sub_dict.add_sub import add, sub
strAdd = "Addition = {0}"
strSub = "Sub = {0}"
print(strAdd.format(add(20,10)))
print(strSub.format(sub(100,50)))