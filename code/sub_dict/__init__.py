print("------------------------------------------------------------")
print("We are currently inside the __init__.py file of sub_dict")

from .add_sub import add, sub
strAdd = "Addition = {0}"
strSub = "Sub = {0}"
print(strAdd.format(add(20,10)))
print(strSub.format(sub(100,50)))
print("------------------------------------------------------------")