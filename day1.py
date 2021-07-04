"""
print ("hello,world") #字符串
print(12346)          #整数
print(1.11)           #小数
print(True,False)     #布尔值
print(())             #元祖
print([])             #数组
print({})             #字典
print("字符串"+"拼接") #字符串拼接
print("字符串"*10)
print(((1+2)*99-100)*2)
print(2>3)
print(1+1==2)
"""
#a=input ("请输入内容：")
#print("input获取的内容：",a)
# a=input("请输入a：")
# b=input("请输入b：")
# print("input获取的内容：",a+b)
#数据类型#
# print(type("aaa"))
# print(type(111))
# print(type(1.11))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))
#字符串转换成其它类型数据，必须满足‘长得像’
# a=float(input("请输入a："))
# b=float(input("请输入b："))
# print("input获取的内容：",a+b)
#len()方法的使用
# a='hghhjhj  jhf'
# print(len(a))

# a="学习python的第一天"
# b="要继续加油!"
# print(a)
# print(b)
# print("a+b的长度：",len(a)+len(b))
#测试第二次向github提交代码
#元组,下标(从零开始编号)
"""a = (1,2,3,4,"字符串","zifuchuan","字符串",True,False)
print (a[4])
#切片
print(a[0:4])   #左闭右开
print(a[:5])
print(a[:])
print(a[1:5])
#方法
print(a.index("字符串"))
print(a.count("字符串"))"""
#二维元组
"""a = (1,2,3,4,"字符串","zifuchuan","字符串",True)
b = (a,"zifuchuan","字符串",0)
print(b[0][2])"""
#元组一旦写好之后是不可以修改的，但是数组可以修改

#数组
"""a = [1,2,3,4,"字符串","zifuchuan","字符串",True,False]
a.append("添加的数据")#只能从尾末插入数据
a.insert(4,"在任意位置插入数据")#insert可以在数组任意位置插入数据
a.pop(3)#类似于剪切的作用
b=a.pop(0)
c=a.pop(0)
#a.clear()
print (a)
print(b+c)
x=["你好","不好"]
a.extend(x)#可以将数组插入数组中
print(a)
a.remove("zifuchuan")#删除某个值
print(a)
a.remove(0)
print(a)
xx=[0,False,True,1]
b=xx.count(0)
print(b)
#下标不要超出范围=越界
xxx=[0,1,2,3]
print(xxx[5])"""
#字典
"""字典的特点
1.字典中的值是没有顺序的
2.字典的结构必须是键值对的结构。key：value
3.字典的取值是通过key取value
4.所有的字符串都要加""
"""
a={"name":"张三","age":26,0:"hahhaha"}
#取值
print(a["name"])
#新增
a["high"]="180cm"
print(a)
#修改
a["name"]=["李四"]
print(a)

b=a.get("name")
print(b)
b=a.pop("name")
print(a)
a.update(name=1111)
print(a)

#get与取值的区别
"""print(a.get("name1"))#返回空
print(a["name1"])#代码会报错"""

#数组和字典的删除
del a["name"]
print(a)
a=[1,2,3]
del a[0]
print(a)

"""
获取用户输入的个人信息并且存储到字典中
个人信息包括了name,age,sex"""
a={"name":"shiyuzhen","age":26,"sex":"女"}
print("用户shiyuzhen的个人信息：",a)

