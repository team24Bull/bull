user_num = []
ran_num = []

def main(user_num, ran_num):
    for i in range(len(user_num)):
        out_count = 0
        if user_num[i] != ran_num[i]:
            out_count += 1
        else:
            pass ## ball이나 strike가 들어가면 좋을 거 같습니다.

    if out_count == len(user_num):
        print('Out!')
