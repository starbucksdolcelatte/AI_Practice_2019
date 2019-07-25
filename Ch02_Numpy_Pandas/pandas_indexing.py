import pandas as pd

# index 직접 설정 가능
d = pd.Series([1, -4, 7], index = ['2019-06-30', '2019-07-01', '2019-07-02'])
print(d)
# 2019-06-30    1
# 2019-07-01   -4
# 2019-07-02    7

# index 직접 설정 가능
a = pd.Series([10,20,30], index = ['SK', 'naver', 'samsung'])
b = pd.Series([100, 200, 300], index = ['naver', 'SK', 'samsung'])

print(a+b)
# SK         210    (10 + 200)
# naver      120    (20 + 100)
# samsung    330    (30 + 300)
# dtype: int64
# 같은 인덱스끼리 더해짐.
