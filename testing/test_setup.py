# -*- coding: utf-8 -*-

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def test_case1():
    print("case1")

def setup_function():
    print("setup function")

def teardown_function():
    print("teardown fruction")


class TestDemo:

    # 类 前后分别执行setup_class teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")

class TestDemo2:

    # 类 前后分别执行setup_class teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")