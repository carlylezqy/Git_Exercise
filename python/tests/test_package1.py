import os 
import sys
class TestModule:
    def test_package1(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(current_path + '/..')
        import module
        
        print("进行中文测试")
        module.package1.package1()