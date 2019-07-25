def main():
    a = [1.23, -2.21, 3.66, -4.25, 5.21, -31.25, 18.87, 1.43, -2.00, -55.21, 25.02]

    # 리스트 a 내의 각각의 원소에 대해서 0보다 크면 1을, 0보다 작거나 같으면 0을 값으로 갖는 리스트를 만들어 봅시다.
    sign_a = [1 if _a > 0 else 0 for _a in a]

    b = [1, 0, 3, -4, 1, 26, 25, 1, 5, 47, 25]

    # 리스트 a와 b의 원소들을 대응시켜 'a[i] - b[i]' 연산을 했을 때, 그 결과가 0보다 크고 1보다 작은 경우 1을, 아닐 경우 0을 값으로 갖는 리스트를 만들어 봅시다.

    c = [1 if (_a - _b > 0) and (_a - _b < 1) else 0 for _a, _b in zip(a,b)]

    b = [1.43, 3.66, -2.14, -55.20]

    # 리스트 a 안에 b의 i번째 원소 b[i]가 있으면 True, 없으면 False를 i번째 원소로 갖는 리스트(1행 4열)를 생성해 봅시다.
    b_in_a = [True if (_b in a) else False for _b in b]

    # 리스트 a 안에 b의 i번째 원소 b[i]가 없으면 True, 있으면 False를 i번째 원소로 갖는 리스트(1행 4열)를 생성해 봅시다.
    b_not_in_a = [True if (_b not in a) else False for _b in b]

    print(sign_a, c, b_in_a, b_not_in_a)

main()
