from Base.base import Base

from page.page_elements import PersonXiangQing
class PeopleXiangQing(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)


    def click_edit_btn(self):
        self.click_ele(PersonXiangQing.edit)


    def get_result(self):
        return [i.text for i in self.find_eles(PersonXiangQing.result)]