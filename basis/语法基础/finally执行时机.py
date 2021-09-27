"""
@Author: yanzx
@Date: 2021-09-27 22:55:58
@Desc:
总结：无论什么情况finally中的代码都可以被执行，也就是在值进行返回的时候，将要返回的值（引用的话就是对象的副本，基本数据类型的话就是值类型）放到一个槽（slot）中，
然后执行finally中的代码，最后进行返回
"""
import unittest


class MyTestFinally(unittest.TestCase):
    def testOne(self):
        try:
            print("I am try")
            print(1 / 0)
        except Exception as e:
            print("I am exception")
            return
        finally:
            print("I am finally")
