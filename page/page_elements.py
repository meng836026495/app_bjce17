
# 所有联系人列表页面
from selenium.webdriver.common.by import By


class AllPeople:
    # 联系人的定位信息
    people = (By.ID, 'com.android.contacts:id/cliv_name_textview')



# 联系人详情页面
class PersonXiangQing:
    # 修改按钮的定位信息
    edit = (By.ID, 'com.android.contacts:id/menu_edit')
    # 返回数据的定位信息
    result = (By.ID, 'com.android.contacts:id/large_title')


# 修改联系人页面
class EditPeople:
    # 用户名输入框的定位信息
    uasername = (By.CLASS_NAME, 'android.widget.EditText')
    # 返回按钮的定位信息
    back = (By.CLASS_NAME, 'android.widget.ImageButton')