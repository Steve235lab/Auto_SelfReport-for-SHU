# -*- coding: utf-8 -*-
"""
Direct_SelfReport.py

Not a released version!
A special edition of project Auto_SelfReport to do SHU self report DIRECTLY whenever it's run.
For most cases, this edition of program is only for Steve to debug and do some tests.

Created on Sat Apr 24 22:49:26 2021

@author: Steve D. J.
"""

#在''中填入学号
ID = ''

#在''中填入密码
Password = ''


from selenium import webdriver
import time


#检索未填报项目，并进行填报
def Search_Unreported():
    print("正在检索未填报项目...\n")
    Unreported_Flag = 0
    for i in range(1,63):
        try:
            temp = driver.find_element_by_xpath('//*[@id="Panel1_DataList1"]/ul/li[' + str(i) + ']')
            #print(temp.text)
            temp_str = temp.text
            str_len = len(temp_str)
            for j in range(0, str_len):
                if temp_str[j] == '(':
                    left_index = j
                elif temp_str[j] == ')':
                    right_index = j
                    state_str = temp_str[left_index+1 : right_index]
                    #print(state_str)
                    if state_str == '未填报，请点击此处补报':
                        Unreported_Flag = 1
                        print("已定位到未填报项目，正在进行填报...\n")
                        try:
                            driver.find_element_by_xpath('//*[@id="Panel1_DataList1"]/ul/li[' + str(i) + ']').click()
                        except:
                            pass
                        #勾选"我承诺..." //*[@id="p1_ChengNuo-inputEl-icon"]
                        driver.find_element_by_xpath('//*[@id="p1_ChengNuo-inputEl-icon"]').click()
                        """#新版"每日一报"系统无需填写具体体温
                        #生成体温并填写
                        tempreture = '%.1f'%(random.uniform(36.0,36.9))
                        driver.find_element_by_xpath('//*[@id="p1_TiWen-inputEl"]').send_keys(str(tempreture))
                        """ 
                        #勾选"良好（体温不高于37.3）" //*[@id="fineui_0-inputEl-icon"]
                        driver.find_element_by_xpath('//*[@id="fineui_0-inputEl-icon"]').click()
                        #勾选"国内" //*[@id="fineui_5-inputEl-icon"]
                        driver.find_element_by_xpath('//*[@id="fineui_5-inputEl-icon"]').click()
                        #勾选"在上海" //*[@id="fineui_7-inputEl-icon"]
                        driver.find_element_by_xpath('//*[@id="fineui_7-inputEl-icon"]').click()
                        #勾选"住校" //*[@id="fineui_9-inputEl-icon"]
                        time.sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="fineui_9-inputEl-icon"]').click()
                        time.sleep(0.5)
                        #勾选"不是家庭地址" //*[@id="fineui_12-inputEl-icon"]
                        driver.find_element_by_xpath('//*[@id="fineui_12-inputEl-icon"]').click()
                        """
                        #勾选"不在校"
                        driver.find_element_by_xpath('//*[@id="fineui_5-inputEl-icon"]').click()
                        #勾选"不到校" 
                        driver.find_element_by_xpath('//*[@id="fineui_10-inputEl-icon"]').click()
                        #勾选"国内"
                        driver.find_element_by_xpath('//*[@id="fineui_17-inputEl-icon"]').click()
                        time.sleep(0.1)
                        #勾选"不在上海"
                        driver.find_element_by_xpath('//*[@id="fineui_8-inputEl-icon"]').click()
                        
                        """
                        """#网页会按照以前的记录默认勾选
                        #勾选"否"
                        driver.find_element_by_xpath('//*[@id="fineui_21-inputEl-icon"]').click()
                        driver.find_element_by_xpath('//*[@id="fineui_27-inputEl-icon"]').click()
                        driver.find_element_by_xpath('//*[@id="fineui_17-inputEl-icon"]').click()
                        driver.find_element_by_xpath('//*[@id="fineui_19-inputEl-icon"]').click()
                        """
                        #点击提交按钮 //*[@id="p1_ctl01_btnSubmit"]
                        driver.find_element_by_xpath('//*[@id="p1_ctl01_btnSubmit"]').click()
                        time.sleep(0.8)
                        #确认对话框-点击"确定"
                        #driver.find_element_by_xpath('//*[@id="fineui_32"]').click() #//*[@id="fineui_42"]
                        for psb_num in range(0, 1024):
                            temp_xpath = '//*[@id="fineui_' + str(psb_num) + '"]'
                            try:
                                YorN = driver.find_element_by_xpath(temp_xpath)
                                temp_str = YorN.text
                                #print(temp_str)
                                if temp_str == '确定':
                                    driver.find_element_by_xpath(temp_xpath).click()
                                    #print("点击了1号确定！")
                                    break
                            except:
                                pass
                        time.sleep(0.2)
                        #提交成功-"确定" 或 "现在还没到晚报时间"-确定
                        for psb_num in range(0, 1024):
                            temp_xpath = '//*[@id="fineui_' + str(psb_num) + '"]'
                            try:
                                YorN = driver.find_element_by_xpath(temp_xpath)
                                temp_str = YorN.text
                                #print(temp_str)
                                if temp_str == '确定':
                                    driver.find_element_by_xpath(temp_xpath).click()
                                    break
                            except:
                                pass

                        #print("点击了2号确定！")
                        time.sleep(0.2)
                        try:
                            #提交成功-"确定"后会回到首页，再次进入"报送历史"进行确认
                            driver.find_element_by_xpath('//*[@id="lnkReportHistory"]').click()
                            i = 1
                            #print("已为您填报: " + temp_str[0 : left_index] + " 使用的体温为" + str(tempreture) + "\n")
                            print("已为您填报: " + temp_str[0 : left_index] + "\n")                        
                        except:
                            """
                            #"现在还没到晚报时间"-确定后返回上一页
                            driver.back()
                            print(temp_str[0 : left_index] + ' 由于"现在还没到晚报时间"原因，未能填报\n')
                            """
                            pass
        except:
            pass
    if Unreported_Flag == 0:
        print("您没有未填报的记录！\n")


if __name__ == '__main__':
    
    print("Copyright (c) 2020-2021 Steve D. J.. All rights reserved.\n")
    print("正在执行Direct Self Report\n")

    #打开Chrome浏览器
    print("正在打开Chrome浏览器...\n")
    try:
        driver = webdriver.Chrome()
        print("已成功打开Chrome浏览器\n")
    except:
        print("未能打开Chrome浏览器，请根据本文件前的'使用须知'第一条检查无误后重新运行此程序\n")
        time.sleep(20)
        exit()
    
    #访问健康之路网页
    time.sleep(1)
    print("正在跳转健康之路网页...\n")
    driver.get('https://selfreport.shu.edu.cn')
    
    #填写账号密码
    print("正在填写账号密码...\n")
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(ID)   
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(Password) 
    time.sleep(0.5)
    
    #点击"登陆"
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    print("登陆成功！\n")
    time.sleep(0.5)
    
    #进入"报送历史"
    driver.find_element_by_xpath('//*[@id="lnkReportHistory"]').click()
    time.sleep(0.5)
    
    #检索未填报项目，并进行填报
    Search_Unreported()

    print("已为您完成每日一报！\n")