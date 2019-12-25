from page.all_person import All_person
from page.people_edit import PeopleEdit
from page.people_xiangqing import PeopleXiangQing


class Page:
    def __init__(self,driver):
        self.driver = driver


    # 定义返回所有联系人页面类
    def get_all_people(self):
        return All_person(self.driver)


    # 定义返回联系人详情页面类
    def get_people_xiangqing(self):
        return PeopleXiangQing(self.driver)

    # 定义返回修改联系人页面类
    def get_edit_people(self):
        return PeopleEdit(self.driver)