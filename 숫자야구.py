import random 

def generate() :
    i = 0
    ans_num = []
    while i < 3 :
        ans = random.randint(0,9)
        if ans in ans_num :
            continue
        ans_num.append(ans)
        i += 1
    return ans_num

def guess() :
    i = 0
    user_guess = []
    print('0~9의 숫자를 입력해 주세요.')
    while i < 3 :
        gue_num = int(input('{}번째 숫자를 입력해 주세요.'.format(i+1)))
        if gue_num < 0 or gue_num > 9 :
            print('범위 밖의 숫자입니다. 다시 입력해 주세요.')
            continue
        if gue_num in user_guess :
            print('중복된 숫자입니다. 다시 입력해 주세요.')
            continue
        else :
            user_guess.append(gue_num)
            i += 1
    return user_guess

def judge(user_guess, ans_num) :
    i = 0
    strike_count = 0
    ball_count = 0
    while i < 3:
        if ans_num[i] == user_guess[i] :
            strike_count += 1
            i += 1
        elif user_guess[i] in ans_num :
            ball_count += 1
            i += 1
        else :
            i += 1
    return strike_count, ball_count

#겜 시작
answer = generate()
tries = 0
print('***숫자 야구 게임을 시작합니다.***')
while True :
    A = guess()
    strike, ball = judge(A, answer)
    if strike < 3 :
        print("===== {}볼 {}스트라이크 입니다.=====".format(ball, strike))
        tries += 1
    else :
        print('축하합니다! 삼진 아웃입니다.')
        print('{}번만에 성공하셨습니다.'.format(tries+1))
        break

    