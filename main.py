import random

def create_num():
	print("난이도 : easy(3), normal(4), hard(5)")
	while True:
		try:
			digit = int(input("난이도를 입력하시오 : "))
			if digit not in [3, 4, 5]:
				print("3, 4, 5 중 난이도를 선택하세요.")
			else:
				break
		except Exception as e:
			print("3, 4, 5 중 난이도를 선택하세요.")
	nums = random.sample(range(10), k=digit)
	return digit, nums


if __name__ == '__main__':
	print(create_num())
