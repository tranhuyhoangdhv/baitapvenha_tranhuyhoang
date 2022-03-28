#trần huy hoàng 
#205752021610030
#bai1.4.1
"""
def sum(a,b):#sum là tên hàm, a,b là tham số truyền vào
    print ("sum is"+str(a+b))
    #tính tổng 2 số 4,5 là
    sum(4,5)
    #tính tổng 2 số 6,7
    sum(6,7)""" #chưa trả về kết quả

#bai1.4.2
"""
def sum(a,b):
    return a+b
c=sum(4,5)
print("sum is : ", str(c))""" #trả về kết quả bằng return

#bai1.4.3
"""
def say_hello(a):
    a="hello"
    print(a)
print(a)"""

#bai1.4.4
"""
a="hello guy!"
def say(a):
    a= " vinh university"
    print (a)
say(a)
print(a)"""

#bai1.4.5
"""
a="hello guy"
def say():
    global a
    a="vinh university"
    print(a)
say()
print(a)
"""
#bai1.4.6
"""
def get_sum(*num):
    tmp = 0
    #duyet cac tham so
    for i in num:
        tmp += i
    return tmp
result = get_sum(1,2,3,4,5)
print(result)
"""
    
