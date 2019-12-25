import pytest,sys,os
sys.path.append(os.getcwd())

from Base.page import Page
from Base.GetDriver import get_android_driver
class Test:
    def setup_class(self):
        self.driver = get_android_driver("com.android.contacts",".activities.PeopleActivity")
        self.page_obj = Page(self.driver)

    @pytest.fixture(scope='class',autouse=True)
    def aaa(self):
        self.page_obj.get_all_people().click_people()

    @pytest.mark.parametrize('a',['menggang','hahaha','happy'])
    def test01(self,a):
        self.page_obj.get_people_xiangqing().click_edit_btn()
        self.page_obj.get_edit_people().edit_username(a)
        assert a in self.page_obj.get_people_xiangqing().get_result()