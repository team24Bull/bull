import random

def create_num():
	print("난이도 : easy(3), normal(4), hard(5)")
	while True:
		digit = input("난이도를 입력하시오 : ")
		if digit not in ['3', '4', '5']:
			print("난이도를 3, 4, 5 중에서 입력해주세요.")
		else:
			digit = int(digit)
			break
	nums = random.sample(range(10), k=digit)
	return digit, nums


# 숫자 맞추기
def get_strike_num(comp, user, n):
    '''
	comp: 랜덤 숫자 리스트
	user: 유저 인풋 숫자 리스트
	n: 난이도
	'''
    strike = 0
    for i in range (n):
        # 값과 위치가 같다면
        if comp[i] == user[i]:
            # strike 값을 증가 시킨다
            strike += 1

    return strike

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

##  out 카운트 하기
def printOutFunc(user_num, nums):
    out_count = 0
    for i in user_num: ## user_nums의 숫자가 nums 안에 없으면 out을 세시오.
        if i not in nums :
            out_count += 1
    return out_count
 

if __name__ == '__main__':
	print(create_num())

