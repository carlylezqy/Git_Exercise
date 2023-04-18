import os 
import sys
import module


if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_path + '/..')
    print("进行中文测试")
    module.package1.package1()