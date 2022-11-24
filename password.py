PASSWORD = 'abc123'
fail = 3
while True:
	password = input('input password:  ')
	if password == PASSWORD:
		print('登入成功')
		break
	else:
		fail = fail - 1
		print(f"wrong answer, 還有{fail}次機會")
		if fail == 0 : 
			break

