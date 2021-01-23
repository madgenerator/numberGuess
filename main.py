import random
# 정답 숫자 생성 : 모두 다를것
answerNum = [0, 0, 0]
answerNum[0] = random.randrange(1, 9, 1)

answerNum[1] = random.randrange(1, 9, 1)
while (answerNum[0] == answerNum[1]):
  answerNum[1] = random.randrange(1, 9, 1)

answerNum[2] = random.randrange(1, 9, 1)
while (answerNum[0] == answerNum[1] or answerNum[1] == answerNum[2]):
  answerNum[2] = random.randrange(1, 9, 1)

print(answerNum)

try_count = 0 # 시도
strike_count = 0 # 스트라이크
ball_count = 0 # 볼 

print("숫자 야구 게임  START!!!")
print("---------------------------")
while ( strike_count < 3 ):
    strike_count = 0
    ball_count = 0
    num = str(input("3개의 숫자를 입력하세요 : "))

    for i in range(0, 3):
        for j in range(0, 3):
            if(i==j):
              if(int(num[i]) == answerNum[j]):
                strike_count += 1
            else:
              if(int(num[i]) == answerNum[j]):
                ball_count += 1

    print("결과 : [", strike_count, "] Strike [", ball_count, "] Ball")
    try_count += 1

print("---------------------------")
print(try_count, "번 만에 정답을 맞추셨습니다.")