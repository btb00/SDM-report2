#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc (unittest.TestCase):

    # --- 1. 有効な同値クラス (Valid Case) ---
    def test_sample1 (self):
        """元のサンプル: 3x7=21"""
        self.assertEqual (21, calc(3,7))

    def test_valid_reverse (self):
        """A > B のパターン (20x10=200)"""
        # 現在のバグだとここで失敗する可能性があります
        self.assertEqual (200, calc(20,10))

    # --- 2. 境界値分析 (Boundary Value Analysis) ---
    def test_boundary_min_valid (self):
        """有効最小値: 1"""
        self.assertEqual (1, calc(1,1))

    def test_boundary_max_valid (self):
        """有効最大値: 999"""
        self.assertEqual (998001, calc(999,999))

    def test_boundary_min_invalid (self):
        """無効境界値: 0"""
        self.assertEqual (-1, calc(0,100))

    def test_boundary_max_invalid (self):
        """無効境界値: 1000"""
        self.assertEqual (-1, calc(1000,10))

    # --- 3. 無効な同値クラス (Invalid Types) ---
    def test_type_string (self):
        """文字列入力"""
        self.assertEqual (-1, calc('a','b'))
        self.assertEqual (-1, calc('10','20'))

    def test_type_float (self):
        """小数入力"""
        self.assertEqual (-1, calc(0.1,999))

if __name__ == '__main__':
    unittest.main()