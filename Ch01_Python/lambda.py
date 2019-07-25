# lambda는 한 줄로 간단히 함수를 만들 수 있는 도구
# 함수명 = lambda 파라미터 : 함수 내부 구현 (리턴값)

add_multi = lambda x, y : [x + y, x * y]
add = lambda x, y, z : x + y + z
three_step = lambda l : [i*3 for i in l]
print(add_multi(3, 4)) # [7, 12]
print(add(10, 20, 30)) # 60
print(three_step(range(0,10))) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
