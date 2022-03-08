
#tim số nguyên tố từ 2 đến N
N  = int(input("danh sách số nguyên tố từ 1 đến --> "))

for n in range (2, N+1):#vi be hơn 2 khong phai la so nguyen to nên ta chi can xet tu 2 den n,
                        #biến n để tạo 1 dăy số hoàn chỉnh từ 2 đến n
    
    songuyento = True # cho trước biến songuyen to 
    for x in range(2, n): #thêm 1 vong lặp nữa đề chạy từ 2 đến n-1(vì n chia cho n thì du 0 nên ta không xét)
        if n % x == 0: #ví dụ xét số 7 trong dãy từ 1 đến 20 chẳng hạn. thì n là 7 và x là 2,3,4,5,6
          songuyento = False
    if songuyento = True:
        print(n);
        
        
        
        
#số nguyên tố là số chi hết cho 1 và chính nó
#tim duoc k số từ 1 đến n-1 mà chia hết cho n

    #ví dụ cho danh sách từ 2 đến 8 là n: 2,3,4,5,6,7,8.
        #lấy danh sách từ 2 đến n-1 là x: 2,3,4,5,6,7.
        # bắt đầu bằng số 2 thi 2 chỉ chia hết cho 2 và 1, không chia het cho bat ki so nao giưa 1 và 2 <=> du o
        #tiêp theo ví dụ số 4 thi đă chia hét cho 2 nên ko phải là số nguyên tố
        # vidu so 6 thi đă chia hết cho 2 và 3 nên không phải số nguyên tố.
        # voi so 7 khong chi het bat ki cho so nào từ 2,3,4,5,6 => là so nguyen to
