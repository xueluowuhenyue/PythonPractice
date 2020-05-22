# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 20:49
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_ddt.py

#ddt data driver test
#数据驱动测试
#安装： pip install ddt

import unittest
from ddt import ddt,data,unpack

test_data_1=[[1,2,3],[3,-2,1]]
test_data_2=[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}]


@ddt #装饰测试类
class TestPringMsg(unittest.TestCase):

    #data这个函数的参数 是*values 是动态参数 ，传递的参数 ，到函数内不会存到一个元组里面
    #再对元组进行遍历 ，取到元组的值之后传递给被装饰的函数的参数名
    # @data([1,2],(4,5,9))#装饰测试用例([1,2,3],(4,5,9))
    # @unpack#对data传递过来的元组子元素进行拆分 要求是可迭代
    # def test_001(self,a,b,expected=None):#如果用了unpack 必须用对应个数的参数名来进行接收
    #     print('我在执行第{}条用例'.format(a))
    #     c=a+b
    #     self.assertEqual(c,expected)
    #     # print('x:',x)
        # a=x[0]
        # b=x[1]
        # c=a+b
        # print('b:',b)
        # print('c:',c)

    @data(*test_data_1)#[1,2,3],[3,-2,1]--->([1,2,3],[3,-2,1])
    # @unpack
    def test_002(self,a):
        c=a[0]+a[1]
        print(c)
        self.assertEqual(c,a[2])
    #[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}]-->加*脱外套
    # ({'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1})
    # @data(*test_data_2)#[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}]
    # @unpack #如果是对字典进行拆分的话 要记得用对应的key的参数名来接收值
    # def test_003(self,dict):
    #     c=dict['a']+dict['b']
    #     self.assertEqual(c,dict['expected'])




