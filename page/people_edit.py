from Base.base import Base
from page.page_elements import EditPeople

class PeopleEdit(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)


    def edit_username(self,text):
        self.send_eles(EditPeople.uasername,0,text)
        self.click_ele(EditPeople.back)



