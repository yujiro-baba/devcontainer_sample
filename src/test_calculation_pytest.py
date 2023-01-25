import os

import pytest

import calculation

is_release = True

# 期待値通りの値が返るかテスト
class TestCal(object):
    @classmethod
    # テスト前に呼び出す処理
    def setup_class(cls):
        print("start")
        cls.cal = calculation.Cal()
        cls.test_dir = 'tmp/test_dir'
        cls.test_file_name = 'test.txt'

    # テスト後に呼び出す処理
    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    # 期待値通りに値を返すかテスト
    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    # 例外処理テスト
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
