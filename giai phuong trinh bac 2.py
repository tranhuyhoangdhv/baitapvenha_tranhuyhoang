import math #Để import một module có vào trong file hiện tại thì mọi người sử dụng từ khóa import import /
models math và gọi thử một số phương thức trong module math
 
"""
# cmt Giải phương trình bậc 2: ax2 + bx + c = 0
# hệ số a: hệ số bậc 2
# hệ số b: hệ số bậc 1
# hệ số c: số hạng tự do
"""
def giaiPTBac2(a, b, c):# def trong python là một từ khóa (keyword) dùng để xác định một hàm. Chúng ta sử dụng def khi khai báo hàm trong python.
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình\
vô nghiệm!"); #"" là trich dan \ dùng để chỉ chung trên 1 dòng, để chỉ rõ sự liên tục dòng 
        else: # 
            print ("""Phương trình có một
nghiệm: x = """, + (-c / b));#trich dan tam """dung de trich dan và comment xuong dong
        return;
 
    # tính delta
    delta = b * b - 4 * a * c;
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a)); #khaibao x1 dạng float và math.sqrt Mô-đun này cung cấp quyền truy cập vào các hàm toán học căn bậc hai
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):# đây là 1 hearder bắt đầu lệnh (với từ khóa) và kết thúc với mộtdầu hai chấm (:) theo sau bởi một suite (khoi lenh )
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else:
        print("Phương trình vô nghiệm!");
    #các khối lệnh
 
# Nhập các hệ số
a = float(input("Nhập hệ số bậc 2, a = "));
b = float(input("Nhập hệ số bậc 1, b = "));
c = float(input("Nhập hằng số tự do, c = "));
# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)
"""het/
ca"""
