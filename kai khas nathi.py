x=[1,2,3]
y=[4,5,6]
#TODO: change this
x_list=[x]*10
y_list=[y]*10
big_list=x_list+y_list
print("x_list contains %d objects"% len(x_list))
print("y_list contains %d objects"%len(y_list))
print("big_list contains %d objects"%len(big_list))
print(x_list)
q=[]
l=0;
for i in x_list:
   q=i
   l+=len(q);
   

print("lenth=",l)


#Testing Code
if x_list.count(x)==10 and y_list.count(y)==10:
    print("Almost there....")
if big_list.count(x)==10 and big_list.count(y)==10:
    print("Great!")
