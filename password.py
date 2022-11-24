PASSWORD = 'abc123'
fail = 3
while fail > 0:
	fail = fail - 1
	password = input('input password:  ')
	if password == PASSWORD:
		print('登入成功')
		break
	else:
		if fail != 0:
			print(f"wrong answer, 還有{fail}次機會")
		else:
			print(f"wrong answer, good bye")

