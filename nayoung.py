def function3(comp, user, n):
    # strike
    strike = 0
    for i in range (n):
        # 값과 위치가 같다면
        if comp[i] == user[i]:
            # strike 값을 증가 시킨다
            strike += 1

    return strike