# up down 게임

# 인원수 설정한다. 최소 3명

# 술래가 술뚜껑을 뒤집어본다.
# 1~100까지의 랜덤 숫자를 확인한다.


# 추측할 숫자를 차례로 맞춰본다.
# 추측한 숫자가 정답보다 크면 up 작으면 down

# 한뷔퀴를 돌기전 정답을 맞춘다면 술래는 술을 마신다.
# 한바퀴 이후 추측한 사람들이 맞춘다면 그사람이 술을 마시며 술래가 된다.


class Player_target:
    """술래"""

    def __init__(self, **kwargs):
        print("술래 : 저는 술래 입니다.")
        self.hold_num = kwargs.get("hold_num")

    def compare_guess(self, guess_num):
        if guess_num == self.hold_num:
            print("정답입니다!!")
            return True
        elif guess_num < self.hold_num:
            print("술래 : UP!")
        else:
            print("술래 : DOWN!")

        return False

    def validate_circle(self, guessor_counts, people_states):
        check_counts = 0

        for person_state in people_states:

            if person_state:
                check_counts += 1
                check_counts = True

        return guessor_counts == check_counts


class Player_guessor():
    """일반인"""

    def __init__(self, is_target, **kwargs):
        self.speak_state = False
        self.id = kwargs.get("id")
        print(f"사람{self.id} : 저는 일반인 입니다.")

    def speak_guess(self):
        guess_number = int(input(f"사람{self.id} :일반인 추측할 번호를 말씀하세요."))
        self.speak_state = True
        return guess_number


# 게이머 설정.
user_count = int(input("플레이 하실 인원을 말씀해주세요."))

if (user_count - 1) < 2:
    print("플레이어 수가 너무 부족합니다. 최소한 3명은 되어있어야 합니다.")

print("게임을 시작합니다.")
print("술래 생성중....")

target = Player_target(isTarget=True, hold_num=40)

nontarget = []
for i in range(0, user_count - 1):
    id = i+1
    nontarget.append(Player_guessor(is_target=False, id=id))





# 게임 시작
is_game_playing = True
while is_game_playing:

    for player_guesser in nontarget:
        guess_num = player_guesser.speak_guess()

        if target.compare_guess(guess_num):
            is_game_playing = False
            break


    # user 생성
