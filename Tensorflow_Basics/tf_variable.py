import tensorflow as tf

# random_normal 텐서플로우 상수 할당
rand_normal = tf.random_normal([2,5], seed = 100)


# random normal 상수를 초기값으로 가지는
# 텐서플로우 변수 할당
varRandNormal = tf.Variable(rand_normal)

# global_variable_initializer()를 init 변수에 설정
init = tf.global_variables_initializer()

with tf.Session() as sess:
    # 세션을 이용해 변수 초기화 실행
    sess.run(init)
    # 세션을 이용해 변수에 들어있는 값 출력
    print(sess.run(varRandNormal))
