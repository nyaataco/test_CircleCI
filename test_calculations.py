'''
PyPro p285
unittestモジュールを使った簡単なテストコードを
CircleCIで動かしてみる

テスト
'''

import unittest

import calculations

class CalculationsTest(unittest.TestCase):
    '''
    割り算する関数をテストする
    '''
    def test_divide_normal(self):
        self.assertEqual(calculations.divide(2, 2), 1)

    def test_divide_contain_zero(self):
        # 結果が１であるため修正
        self.assertEqual(calculations.divide(0, 1), 1)


if __name__ == '__main__':
    unittest.main()