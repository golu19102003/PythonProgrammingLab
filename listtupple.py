my_list = [10,20,30,40,50]
print("original list:",my_list)
my_list.append(60)
my_list.remove(20)
print("modified list:",my_list)
print("first element in list:",my_list[0])
print("Second element in list:",my_list[-1])
my_tuple=(100,200,300,400,500)
print("\n original tuple:",my_tuple)
print("first element in tuple:",my_tuple[0])
print("Second element in tuple:",my_tuple[-1])
try :
    my_tuple[-1] = 250
except TypeError as e:
    print("Error:",e)