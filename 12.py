from roboid import *

hamster = Hamster()

count = 0

while True:
    # 선 감지
    if hamster.left_floor() < 20 or hamster.right_floor() < 20:

        # 부저 소리
        hamster.buzzer(440)   # 440Hz
        wait(300)
        hamster.buzzer(0)

        # 카운트 증가
        count += 1
        print("선 감지:", count)

        # 5번 만나면 종료
        if count >= 5:
            hamster.stop()
            break

        # 뒤로 이동
        hamster.wheels(-30, -30)
        wait(500)

        # 오른쪽 회전
        hamster.wheels(30, -30)
        wait(500)

    else:
        # 앞으로 이동
        hamster.wheels(30, 30)

    wait(20)

# 완전히 정지
hamster.stop()
