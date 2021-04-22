password_c = 'a123456'
i = 3
while True:
    password_a = input('請輸入密碼:')
    if password_a == password_c:
        print('登入成功!')
        break
    else:
        i = i - 1
        print('密碼錯誤! 還有',i, '次機會')
        if i == 0:
            print('錯誤達三次，已無法登入。')
            break 