from pip._internal.utils import logging
from selenium.webdriver.common.by import By


def find_Element(self, type, value):
    '''
    method explain:查找某个元素
    parameter explain: 【type】 取值的类型包括：id\name\class_name...   【value】根据type的类型给值
    Usage:
        device.find_Element('name',"我的認證")
    '''
    print("执行--------find_Element-------方法")
    try:
        if type == 'id':
            try:
                return self.driver.find_element(By.ID, value)  # 查找ID元素，存在则直接返回
            except Exception as e:
                #appium存在元素则直接返回，不存在则跑出异常，因此必须用异常来处理不存在元素的情况
                print("未找到%type--%value" ,type, value)
                return False
            # 查找ID元素，不存在则返回False
        elif type == 'name':
            try:
                return self.driver.find_element(By.NAME, value)
            except Exception as e:
                print("未找到%type--%value" % (type, value))
                return False
        elif type=='class':
            try:
                return self.driver.find_element(By.CLASS_NAME, value)
            except Exception as e:
                print("未找到%type--%value" % (type, value))
                return False
    except:
        print("此处已抛异常---------------find_Element")
        self.take_screenShot("find_Element")
    assert 'find_Element'

    def click(self):
        '''
    method explain:查找某个元素
    parameter explain: 【type】 取值的类型   【value】根据type的类型给值
    Undertake method:device.find_Element(type,value)
    Usage:
        name_value == device.find_Element(type = 'name',value="我的認證")
        name_value.click()
    '''
        self.find_Element(type, self.value).click()