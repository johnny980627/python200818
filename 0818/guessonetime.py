import random
ans = int(input("請輸入數字:"))
num = random.randint(1, 10)


if num == ans:
    print("恭喜答對!")
else:
    print("答錯了!")