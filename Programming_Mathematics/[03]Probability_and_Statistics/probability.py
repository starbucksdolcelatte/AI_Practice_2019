'''
동전을 던져서 앞면이 나올 확률은 일반적이라면 1/2입니다.
그러나 이는 앞면이 나올 확률과 뒷면이 나올 확률이 같다는 전제하에 계산된 확률입니다.
실제로 동전을 던져보아 나온 결과를 바탕으로 계산한 통계적 확률은 다를 수도 있습니다.

동전이 하나 있습니다.
이 동전은 각 면의 무게가 다르게끔 제작되어
던졌을때 앞면과 뒷면이 나올 확률이 다릅니다.
앞면이 나올 확률을 구하는 방법은 실제로 던져보아 빈도를 세는 방법 뿐입니다.
동전의 앞면이 나올 확률이 0.5±0.001의 범위 내에서라면 정상적인 동전이라고 판단합니다.
주어진 동전이 정상인지 판단하는 함수를 작성해 봅시다.

여기서 난 에러는 "충분히 큰 수"만큼 동전을 던지지 않았기 때문에 난 에러.
동전을 던지는 횟수를 늘리니 real_coin은 0.5에 근사하여 에러 해결.
'''
import coin

def stat_prob(coin):
    # To-do
    H = 0 #Head
    T = 0 #Tail

    for i in range(1000000):
        if (coin.toss()=='H'):
            H += 1
        else:
            T += 1
    PH = H/1000000
    print(PH)
    if PH >= 0.499 and PH <= 0.501:
        return True
    else:
        return False



real_coin = coin.Coin(0.5)
fake_coin = coin.Coin(0.8)
print(stat_prob(real_coin))
print(stat_prob(fake_coin))
