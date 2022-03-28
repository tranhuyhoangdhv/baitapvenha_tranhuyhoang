#trần huy hoàng
#msv 205752021610030
#bai2_1.4.1

"""n1=int(input("enter n1 value"));
n2=int(input("enter n2 value"));
if n1>n2:
    print("n1 is big ")
else:
    print("n2 is big ")"""#đã sửa lỗi

#bai2_1.4.2
"""
import math;
x1 = int(input("enter x1--->"))
y1 = int(input("enter y1--->"))
x2 = int(input("enter x2--->"))
y2 = int(input("enter y2--->"))
d1 = (x2-x1)*(x2-x1);
d2 = (y2-y1)*(y2-y1);
res = math.sqrt(d2+d1)
print ("distance between too points:", res);"""#nhập hai điểm và tính khoảng cách

#bai2_1.4.3
"""
n = int(input("enter a number ------>"))
if n % 2 == 0:
    print("Even Number  !")
else :
    print("ODD Number !")"""#kiểm tra một số chẵn hay lẻ

#bai2_1.4.4
"""
i=1;
for j in range(2,10):
    print ("i:",i,"j:",j)
    print (i,"/",j)
    print (i/j)"""#số nghịch đảo từ a đến b

#bai2_1.4.5
"""
n=int(input("enter a number: "))
while n>0:
    print(n)
    n = n-1;""" #nhập và in ra màn hình từ n đến 0

#bai2_1.4.6
"""
j = [];#tạo một list trống
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))#apppend dùng để nhập i vào
print(",".join(j))# tìm số chia hết cho 7 và ko chia hết cho 5 trong khoảng 2000-3201
"""

#bai2_1.4.7
"""
n=int(input("enter a number ------>"))
d=dict()#dict là 1 thu vien trong
for i in range (1,n-1):
    d[i]=i*i# nhập i vào d()
print(d)""" #in ra dãy số bình phương của 1 đến n

#bai2_1.4.8
"""
a,b = 1,2
total = 0
print (a,end=" ")
while (a<=40000000-1):
    if a%2==0:
        total += a#total=total+a
    a, b = b, a+b
    print(a,end=" ")
print("\n sum of prime number term in fibonacci series : ",total)""" # viết chương trình dãy số flotino duoi 4000000 và tính tổng các số chẵn đã in ra  

#bai2_1.4.9
"""
str = input("enter a string: ")
dict = {}
for n in str :
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)""" #đếm số kí tư trong 1 xâu lưu theo cấu trúc từ điển dict

#bai2_1.4.10
"""
a="hi i am python programmer "
b=a.split() # tách xâu
print (b)
c=" ".join(b)#nhập xâu
print(c)""" #tách nhập xâu

#bai2_1.4.11
"""
l=[1, "python",4,7]
k=["cse",2,"guntur",8]
m=[]
m.append(l);
m.append(k);
print(m)
d={1:1,2:k,"combine_list":m}
print(d)"""

#bai2_1.4.12
"""
import re
value = []
items=[x for x in input("nhap mat khau: ").splt(',')]

for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif not re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))"""# nhập mật khẩu

#bai2_1.4.13
"""
from math import sqrt

def giaiptbac2(a,b,c):

     if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm!")
            else:
                print("Phương trình vô nghiệm!")
        else:
           if c == 0:
                print("Phương trình có 1 nghiệm x = 0")
           else:
                print("Phương trình có 1 nghiệm x = ", -c / b)
  else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

giaiptbac2(a,b,c);""" #giải phương tŕnh bậc 2

#câu hỏi kiểm tra


    



    




    



