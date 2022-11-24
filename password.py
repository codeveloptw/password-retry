PASSWORD = 'abc123'
fail = 3
while True:
	password = input('input password:  ')
	if password == PASSWORD:
		print('登入成功')
		break
	if password != PASSWORD:
		print('wrong answer')
		fail = fail - 1
		if fail <= 0 : 
			break
		else:
			print(f"還有{fail}機會")
