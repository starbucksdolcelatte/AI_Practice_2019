import tensorflow as tf

# 입력해 줄 데이터를 할당합니다.
x = [[10, 10, 10], [20, 20, 20]]
y = [[100, 100, 100], [200, 200, 200]]

# placeholder 생성합니다.
X = tf.placeholder(tf.int32, shape = (None, 3))
Y = tf.placeholder(tf.int32, shape = (None, 3))

# placeholder X와 Y를 element-wise 곱 연산을 합니다.
mul = X * Y

# 세션을 생성합니다.
with tf.Session() as sess:
    # 데이터를 feed 해주고 sess을 실행해
    # 연산 결과를 출력합니다.
    print(sess.run(mul, feed_dict = {X:x, Y:y}))
