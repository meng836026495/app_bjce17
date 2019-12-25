import pytest
import yaml,os,sys
sys.path.append(os.getcwd())
from Base.GetData import get_yaml_data
# def get_data():
#     arr = []
#     data = GETDATA().get_yaml_data('sum_data.yml')
#     for i in data.values():
#         arr.append(tuple(i.values()))
#
#     return arr




class Test:
    # @pytest.mark.parametrize('a,b,c',get_data())
    @pytest.mark.parametrize('a,b,c',get_yaml_data('sum_data.yml'))
    def test_sum(self,a,b,c):
        assert a+b==c
