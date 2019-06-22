def bayesian(mails, spam, key):
    # To-do
    '''
    P(A|B) : 특정 키워드를 포함한 메일을 받았을 때, 이 메일이 스팸일 확률
    P(B) : 특정 키워드를 포함한 메일을 받을 확률 = 특정 키워드 메일 수 / 전체 메일 수
    P(A) : 스팸 메일을 받을 확률 = 스팸 메일 수 / 전체 메일 수

    P(A|B) = (P(A) * P(B|A)) / P(B)
           = (P(A) * (P(B∩A) / P(A))) / P(B)
    '''

    total = len(mails) # 전체 경우의 수
    PA = sum(spam)/total # 스팸메일 확률
    B = [key in x for x in mails] # mails에 key가 있으면 True, 없으면 False
    PB = sum(B)/total # 메일에 key가 있을 확률

    # B와 A의 교집합 경우의 수
    # 메일에 key가 있을 때(즉 B == True일 때) spam == True일 경우
    BnA = [spam[i] * B[i] for i in range(len(B))] #bitwise AND

    # B와 A의 교집합 확률
    P_BnA = sum(BnA)/total
    
    return (PA * (P_BnA / PA)) / PB


print(bayesian(['hello my name is elice', 'free money for you', 'we all lie'], [False, True, False], 'free'))
