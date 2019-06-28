import tensorflow as tf

output_weight = 0
output_bias = 0

# 학습할 step의 수
train_step = 500
learning_rate = 0.05 #0.1로 했더니 W와 b가 미쳐날뛰어서 줄였다.

x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

# W와 b에는 랜덤 값을 준다.
W = tf.Variable(tf.random_normal([1]), dtype=tf.float32)
b = tf.Variable(tf.random_normal([1]), dtype=tf.float32)

# 데이터가 들어갈 placeholder를 생성
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# hypothesis의 식을 적어줍니다.
# y = W^T * X + b
hypothesis = tf.add(W*X, b)

# cost function의 식
# tf.reduce_mean은 평균을 구하는 함수
# tf.square는 제곱을 하는 함수
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

# 그레디언트 디센트라는 함수 최적화 알고리즘을 사용해 cost function을 최소화한다.
optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)

# cost function을 optimizer를 이용해 최소화한다.
train = optimizer.minimize(cost)


with tf.Session() as sess:
    # variable 값 초기화
    init = tf.global_variables_initializer()
    sess.run(init)
    for step in range(train_step):
        # train 변수를 통해 optimizer로 cost function을 최소화
        sess.run(train, feed_dict = {X : x_data, Y : y_data})

        output_weight = sess.run(W)[0]
        output_bias =  sess.run(b)[0]
        if step % 100 == 9:
            print(step)
            print('cost : ',sess.run(cost, feed_dict={X: x_data, Y: y_data}))
            print('weight : ', sess.run(W)[0])
            print('bias : ', sess.run(b)[0])
            print()
