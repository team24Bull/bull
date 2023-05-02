
def bull_input(digits):	
	print("정답으로 생각하는 값을 입력하세요.")
	input_value = input()
	# print(len(set(input_value)))
	# print(type(input_value))

	try:
		#정수검사
		if(input_value.isnumeric() == False):
			print("입력값이 정수가 아닙니다.")
		elif (len(set(input_value)) != len(input_value)):
			print("입력값에 중복이 있습니다.")
		#자릿수검사
		elif (len(input_value) != digits):
			print("입력값의 자릿수가 다릅니다.")
		else:
			return int(input_value)			
	except Exception as e:
		print(e)
		print("유효한 입력이 아닙니다")

if __name__ == '__main__':
	print(bull_input(5))
	print("Hello World")
