# [출처] 파이썬#52 - 파이선 로또 번호 생성기, Python Lotto|작성자 남박사

import random
while(1):

    lotto = []
    rnd_num = random.randint(1, 45)

    for i in range(6):
        while rnd_num in lotto:
            rnd_num = random.randint(1, 45)
        lotto.append(rnd_num)

    lotto.sort()
    # if lotto == [1,2,3,4,5,6]:
    #     break

    print(f"로또번호: {lotto}")
