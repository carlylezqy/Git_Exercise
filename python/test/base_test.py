import os; current_path = os.path.dirname(os.path.abspath(__file__))
import sys; sys.path.append(current_path + '/..')

import module
if __name__ == "__main__":
    print("进行中文测试")
    module.package1.package1()