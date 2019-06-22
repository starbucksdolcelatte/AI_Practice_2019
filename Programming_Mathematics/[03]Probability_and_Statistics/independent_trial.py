'''
독립시행에서의 확률 구하기
p 는 어떤 독립사건 A가 일어날 확률(다음 시행에 영향을 주지 않는다)
n 은 총 시행 횟수
r 은 어떤 사건이 일어나는 횟수

어떤 독립사건 A가 일어날 확률을 구하시오.
'''
def shoot_prob(p, n, r):
    # To-do
    s = 1
    m = 1
    for i in range(r):
        s *= (n-i)
        m *= (i+1)
    C = s/m
    return (p**r)*((1-p)**(n-r))*C



print(shoot_prob(0.3, 5, 1))
