from Base.base import Base
from page.page_elements import AllPeople

class All_person(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)


    def click_people(self):
        self.click_ele(AllPeople.people)
