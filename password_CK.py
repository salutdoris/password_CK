password_c = 'a123456'
i = 3
while i > 0:
    password_a = input('請輸入密碼:')
    if password_a == password_c:
        print('登入成功!')
        break
    else:
        i = i - 1
        if i > 0:
            print('密碼錯誤! 還有',i, '次機會')
        elif i == 0:
            print('錯誤達三次，已無法輸入')