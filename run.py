import pytest
import os


if __name__ == '__main__':
    pytest.main(['--alluredir', './temp'])
    os.system('allure generate ./temp/ -o ./report/ --clean')