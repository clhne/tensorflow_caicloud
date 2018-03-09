#-*-coding:utf-8-*-
import tensorflow as tf
#tf.constant是一个计算,其结果保存为一个张量
a = tf.constant([1.0, 2.0], name = "a")
b = tf.constant([4.0, 9.0], name = "b")
result = tf.add(a, b, name = "add")
print result

