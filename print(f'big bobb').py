1 import random
    2
    3 def play_game():
    4     # 1. 컴퓨터가 무작위 숫자 선택 (1부터 100 사이)
    5     secret_number = random.randint(1, 100)
    6     attempts = 0
    7     print("숫자 맞추기 게임을 시작합니다! 1부터 100 사이의 숫자를 맞춰보세요.")
    8
    9     while True:
   10         try:
   11             # 2. 사용자로부터 숫자 입력 받기
   12             guess = int(input("숫자를 입력하세요: "))
   13             attempts += 1
   14
   15             # 3. 힌트 주기
   16             if guess < secret_number:
   17                 print("더 높게!")
   18             elif guess > secret_number:
   19                 print("더 낮게!")
   20             else:
   21                 # 4. 정답 맞췄을 때
   22                 print(f"축하합니다! {secret_number}를 {attempts}번 만에 맞히셨습니다!")
   23                 break
   24         except ValueError:
   25             print("유효한 숫자를 입력해주세요.")
   26
   27 if __name__ == "__main__":
   28     play_game()
