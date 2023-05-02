def cows(user:list, answer:list):
    cow_count = 0
    for i in user:
        if i in answer and user.index(i) != answer.index(i):
            cow_count += 1
    return 'cows: ' + str(cow_count)
