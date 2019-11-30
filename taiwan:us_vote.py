country = input('請問你是哪國人： ') #國家
age = input('請問年齡: ')
age = int(age)
if country == '台灣':
    if age >= 20:
        print('你可以投票！')
    else:
        print('你還不能投票！')
elif country == '美國':
    if age >= 18:
        print('你可以投票！')
    else:
        print('你還不能投票！')
else:
    print('只能輸入 台灣/美國')
