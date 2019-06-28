import tensorflow as tf

# 텐서플로우 상수 three, four 선언

three = tf.constant(3)
four = tf.constant(4)

with tf.Session() as sess2:
    print("변수 three 에 들어간 텐서플로우 상수 값 : ", sess2.run(three))
    print("변수 four 에 들어간 텐서플로우 상수 값 : ", sess2.run(four))
