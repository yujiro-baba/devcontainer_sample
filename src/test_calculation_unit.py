import unittest

import calculation

# クラスCalのテストを行うクラス
class CalTest(unittest.TestCase):
    # テスト前に呼び出される前処理
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    # テスト後に呼び出される
    def tearDown(self):
        print('clean up')

    # 期待値通りの値が返るかテスト
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    # 例外テスト
    # ValueErrorが出力されるかテスト
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

if __name__ == "__main__":
    unittest.main()
