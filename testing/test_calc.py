# -*- coding: utf-8 -*-
import pytest

from pythoncode.calculator import Calculator

def test_a():
    print('test case a')

class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[100,100,200],[-1,-1,-2],[1,0,1]
    ],ids=['int_case','bignum_case','float_case','zero_case'])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_add_float(self,a,b,expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b', [
        [0.1, 0], [10, 0]
    ])
    def test_dev_zero(self,a,b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(1,0)