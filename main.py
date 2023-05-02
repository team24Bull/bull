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

def balls(user:list, answer:list):
    ball_count = 0
    for i in user:
        if i in answer and user.index(i) != answer.index(i):
            ball_count += 1
    return  'balls: ' + str(ball_count)

if __name__ == '__main__':
	print(create_num())
