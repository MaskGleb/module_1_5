immutable_var=1, 2, "один", "два", True, False
print(immutable_var)
#immutable_var[0]=2 # ошибка так как элемент кортежа заранее неизменяемый
#print(immutable_var)
mutable_list=[1, 2, "один","два",True,False]
print(mutable_list)
mutable_list[0]=777
mutable_list.remove("один")
mutable_list.extend("True")
mutable_list.extend([0, 3])
print(mutable_list)