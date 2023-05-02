import random


def create_num():
    '''
    난이도 설정 및 랜덤으로 리스트 생성
    '''
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

def balls(user:list, answer:list):
    '''
    ball 여부 판단
    '''
    ball_count = 0
    for i in user:
        if (i in answer) and (user.index(i) != answer.index(i)):
            ball_count += 1
    return  ball_count


def get_strike_num(comp, user, n):
    '''
	comp: 랜덤 숫자 리스트
	user: 유저 인풋 숫자 리스트
	n: 난이도
	'''
    strike = 0
    for i in range (n):
        # 값과 위치가 같다면
        if comp[i] == int(user[i]):
            # strike 값을 증가 시킨다
            strike += 1

    return strike

def bull_input(digits):	
	'''
	사용자가 예상하는 숫자리스트 입력
	'''
	input_value = input('정답으로 생각하는 값을 입력하세요.: ')

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
			return list(map(int,list(input_value)))		
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

def play_game():
    player_num = int(input("input player number :"))

    for i in range(player_num):
        player = input("input youre name: ")
        diff,com_list = create_num()
        count = 0
        while True:
            user_list = bull_input(diff)
            strike_num = get_strike_num(com_list,user_list,diff) 
            ball_num = balls(user_list,com_list)
            out_num = printOutFunc(user_list , com_list)
            print("strike : {} , ball : {} , out : {}".format(strike_num , ball_num , out_num))
            count +=1
            if strike_num == diff :
                print('End turn player : {} , count : {}'.format(player,count))
                break
	
        


if __name__ == '__main__':
	play_game()
