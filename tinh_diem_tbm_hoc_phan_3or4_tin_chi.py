#tranhuyhoang
print("số tín chỉ là ( 3 or 4  )")
x = float(input())
if x == 3:
    print("enter midterm exam scores(GK): ")
    a = float(input())
    print("enter final exam score(CK): ")
    b = float(input())
    print("enter attendance points(CC):")
    c = float(input())
    print("enter course record score(HSHP):")
    d = float(input())
    s = a * 0.2 + b * 0.5 + c * 0.1 + d * 0.2
else:
    if x == 4:
        print("enter midterm exam scores(GK1): ")
        a = float(input())
        print("enter midterm exam scores(GK2): ")
        e = float(input())
        print("enter final exam score(CK): ")
        b = float(input())
        print("enter attendance points(CC):")
        c = float(input())
        print("enter course record score(HSHP):")
        d = float(input())
        s = a * 0.1 + e * 0.1 + b * 0.5 + c * 0.1 + d * 0.2
    else:
        print("vui long nhap lai !")
if s >= 4:
    if s > 5.4:
        if s > 6.9:
            if s > 8.4:
                print("xếp loại A")
            else:
                print("xếp loại B ")
        else:
            print("xếp loại C  ")
    else:
        print("xep loai D ")
else:
    print("chưa đủ điều kiện qua môn !")
    print("xếp loại F ")
print("average of subject(TBM)is: " + str(s))
