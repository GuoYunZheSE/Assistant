# @Date    : 08:48 03/26/2020
# @Author  : ClassicalPi
# @FileName: Assistant.py
# @Software: PyCharm

import sys
from io import StringIO
import contextlib
import pexpect
import time
from Assistant import Assistant
class DS2:

    def __init__(self):
        self.number=4
        self.assistant=Assistant()

    def exercise1(self,ans:str)->[int,str]:
        if ans=="" or ans==" ":
            return [0,"题目未完成"]
        dict={
            100:"结果正确，并且使用input，有中文提示",
            80:"结果正确，但是没有符合题目规范",
            60: "输出结果不正确，思路正确",
            40:"输出结果不正确，思路部分正确，不同位置的相同字符都会被代替",
            20:"输出结果不正确，思路部分正确",
            0:"输出结果不正确，思路不正确"
        }
        for i in range(2):
            try:
                scope={}
                exec (ans,scope)
            except:
                print("语法错误")
        grade=int(input("100|80|60|40|20|0"))
        print("\t第一题得分:{} 评语:{}".format(grade,dict[grade]))
        return [grade,dict[grade]]

    def exercise3(self,ans:str)->[int,str]:
        grade=0
        comment=""
        ans=ans.split('\n')
        if len(ans)==0:
            comment="该题未完成！"
            return [0,comment]
        Reference_answer=['!','e','HHH',"Hel"]
        for i in range(len(ans)):
            if ans[i]==Reference_answer[i]:
                if i==0:
                    grade+=25
                if i == 1:
                    grade += 25
                if i == 2:
                    grade += 25
                if i == 3:
                    grade += 25
                comment += "第{}行输出正确 ".format(i)
            else:
                comment+="第{}行出错，应该是:{}".format(i,Reference_answer[i])

        print("\t第三题得分:{} 评语:{}".format(grade,comment))
        return [grade,comment]


    def exercise2(self,ans:str)->[int,str]:
        grade=0
        comment=""
        ans=ans.split('\n')
        if len(ans)==0:
            comment="该题未完成！"
            return [0,comment]
        Reference_answer=['abc','abcbc','abcbcc']
        for i in range(len(ans)):
            if ans[i]==Reference_answer[i]:
                if i==0:
                    grade+=30
                if i == 1:
                    grade += 30
                if i == 2:
                    grade += 40
                comment += "第{}行输出正确 ".format(i)
            else:
                comment+="第{}行出错，应该是:{}".format(i,Reference_answer[i])
        print("\t第二题得分:{} 评语:{}".format(grade,comment))
        return [grade,comment]


    def giveGrade(self,ans_id:str,options_name:str,remark_name:str,exercise_number:int):
        function_map={
            1:self.exercise1,
            2:self.exercise2,
            3:self.exercise3
        }
        ans=self.assistant.chrome.find_element_by_id(ans_id).text
        grade,comment=function_map[exercise_number](ans)
        options = self.assistant.chrome.find_elements_by_name(options_name)
        options[int(grade / 10)].click()
        remark = self.assistant.chrome.find_element_by_name(remark_name)
        remark.send_keys(comment)

    def passAll(self):
        info=self.assistant.chrome.find_element_by_id("cmdNextStudent")
        student_left=info.get_attribute('value').split('(')
        student_left=int(student_left[1].strip(')'))
        dict={
            1:{
                "ans_id":"a439",
                "options_name":"radio439",
                "remark_name":"txtRemark439"
            },
            2: {
                "ans_id": "a339",
                "options_name": "radio339",
                "remark_name": "txtRemark339"
            },
            3: {
                "ans_id": "a396",
                "options_name": "radio396",
                "remark_name": "txtRemark396"
            }
        }
        while student_left>=0:
            print("{}: Student-{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),student_left))
            student_left-=1
            for i in dict.keys():
                self.giveGrade(
                    ans_id=dict[i]["ans_id"],
                    options_name=dict[i]["options_name"],
                    remark_name=dict[i]["remark_name"],
                    exercise_number=int(i)
                )
            print(
                "{}:Student-{}评分完成，前往下一评分页面".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), student_left + 1))
            self.assistant.chrome.find_element_by_id("cmdNextStudent").click()
            self.assistant.chrome.implicitly_wait(2)

if __name__ == '__main__':
    ds1=DS2()
    ds1.assistant.login("http://1024.se.scut.edu.cn/")
    ds1.assistant.gotoAssignment("课后练习（基本数据2）")
    ds1.assistant.checkAssignment()
    ds1.passAll()