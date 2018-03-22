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
