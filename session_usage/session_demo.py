#-*-coding:utf-8-*-
#tf使用会话的两种模式
#1.调用会话生成函数和关闭会话函数:
'''
sess = tf.Session()
sess.run(...)
sess.close()
'''
#2.使用python的上下文管理器,避免退出时资源释放的问题:
'''
with tf.Session() as sess:
    sess.run(...)
'''
import tensorflow as tf
a = tf.constant(3)
b = tf.constant(9)
result = a + b
'''
# method 1
sess = tf.Session()
with sess.as_default():
    print(result.eval())
# method 2
sess = tf.Session()
print(sess.run(result))
# method 3
sess = tf.Session()
print(result.eval(session = sess))
# method 4
sess = tf.InteractiveSession()
print(result.eval())
sess.close()
'''
# method 5 通过ConfigProto可以配置类似并行的线程数,GPU分配策略,运算超时时间等参数,allow_soft_placement为True,当某些运算无法被当前GPU支持时,可以自动调整到CPU上,而不是报错,log_device_placement为True时日志中将会记录每个节点被安排到哪个设备上以方便调试,而在生产环境中将这个参数设置为False可以减少日志量.
config = tf.ConfigProto(allow_soft_placement=True,log_device_placement=True)
sess1 = tf.InteractiveSession(config = config)
sess2 = tf.InteractiveSession(config = config)
print(sess1.run(result))
print(sess2.run(result))

