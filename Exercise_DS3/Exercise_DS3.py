# @Date    : 18:33 04/04/2020
# @Author  : ClassicalPi
# @FileName: Exercise_DS3.py
# @Software: PyCharm

import time
from Assistant import Assistant


class DS3:
    def __init__(self):
        self.number=5
        self.assistant=Assistant()

    def exercise1(self,ans:str)->[int,str]:
        def test(n:str):
            s = 0
            for i in range(1,eval(n)+1,2):
                s = s + i
            return s
        comment=""
        dict={
            100:"结果正确，完全符合题目要求",
            80:"轻微错误，整体思路正确",
            70:"第二个空正确，第一个不正确",
            30:"第一个空正确，第二个不正确",
            0:"语法思路均不正确"
        }
        ans=ans.split('\n')

        if len(ans)<2:
            print("答案不完整，请检查")
            return [0,"答案不完整，请检查"]

        for j in range(len(ans)):
            for i in range(0,len(ans[j])):
                if ord(ans[j][i])>=97 and ord(ans[j][i])<=122:
                    ans[j]=ans[j][i::]
                    break
        scope={}
        expr="""n ='{}'\n{}\nfor i in {}:\n\ts=s+i\nprint(s)"""
        for case in [1,98,21321312]:
            try:
                exec (expr.format(case,ans[0],ans[1]),scope)
                if scope['s']==test("{}".format(case)):
                    comment+="测试数据{}测试成功;".format(case)
                else:
                    comment += "测试数据{}测试失败，原因：结果错误，应该是:{}而非{}".format(case,test("{}".format(case)),scope['s'])
                    print("\t"+comment)
                    grade = input("答案一:{}\n答案二:{}\n请输入评分:".format(ans[0], ans[1]))
                    print("\t第一题得分:{} 评语:{}".format(grade, comment))
                    return [int(grade), comment]
            except Exception:
                comment+="测试数据{}测试失败，原因：语法错误".format(case)
                print("\t"+comment)
                grade=input("答案一:{}\n答案二:{}\n请输入评分:".format(ans[0],ans[1]))
                print("\t第一题得分:{} 评语:{}".format(grade, comment))
                return [int(grade), comment]
        print("\t第一题得分:{} 评语:{}".format(100,comment))
        return [100,comment]

    def exercise2(self,ans:str)->[int,str]:
        grade=0
        comment=""
        ans=ans.split('\n')
        if len(ans)==0:
            comment="该题未完成！"
            return [0,comment]
        Reference_answer=['1 ','2 4 ','3 6 9 ','4 8 12 16 ']
        if len(ans)>len(Reference_answer):
            grade = int(input("第二题手动评分"))
            comment="输入的答案规模大于参考答案规模，视情况给分"
            return [grade, comment]
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
        print("\t第二题得分:{} 评语:{}".format(grade,comment))
        if grade!=100:
            grade=int(input("手动评分"))
            if grade==80:
                comment+=" 请不要忘记行末有空格"
        return [grade, comment]

    def exercise3(self,ans:str)->[int,str]:
        grade=0
        comment=""
        ans=ans.split('\n')
        if len(ans)==0:
            comment="该题未完成！"
            return [0,comment]
        Reference_answer=["53","出错了","程序结束"]
        if len(ans)>len(Reference_answer):
            grade = int(input("\t第三题手动评分"))
            comment="输入的答案规模大于参考答案规模，视情况给分"
            return [grade, comment]
        for i in range(len(ans)):
            if ans[i]==Reference_answer[i]:
                if i==0:
                    grade+=40
                if i == 1:
                    grade += 40
                if i == 2:
                    grade += 20
                comment += "第{}行输出正确 ".format(i)
            else:
                comment+="第{}行出错，应该是:{}".format(i,Reference_answer[i])
        print("\t第三题得分:{} 评语:{}".format(grade,comment))
        return [grade, comment]

    def exercise4(self,ans:str)->[int,str]:
        if ans=="" or ans==" ":
            return [0,"题目未完成"]
        def test(a:int,b:int):
            i = a
            k = 0
            while i <= b:
                print(i, end='')
                i = i + 1
                k = k + 1  # 记录每行5个数
                if k % 5 == 0:
                    print()
                elif i != b + 1:  # 最后一个数字不要输出,
                    print(',', end='')
        dict={
            100:"结果正确，并且使用input，有中文提示",
            90:"结果正确，但是没有符合题目规范",
            85: "能运行但有小错误，思路正确",
            80: "行尾还是有逗号，思路正确",
            50:"语法错误，但是整体思路正确",
            20:"输出结果不正确，思路部分正确",
            0:"输出结果不正确，思路不正确"
        }
        for testcase in [[1,5]]:
            try:
                scope={}
                exec (ans,scope)
            except:
                print("语法错误")
        grade=int(input("{}".format(dict.keys())))
        print("\t第四题得分:{} 评语:{}".format(grade,dict[grade]))
        return [grade,dict[grade]]

    def exercise5(self,ans:str)->[int,str]:
        if ans=="" or ans==" ":
            return [0,"题目未完成"]
        dict={
            100:"结果正确，符合要求",
            50:"语法错误或者输出的不是完数的数量，但是整体思路正确",
            20:"输出结果不正确，思路部分正确",
            0:"输出结果不正确，思路不正确"
        }
        try:
            scope={}
            exec (ans,scope)
        except:
            print("语法错误")
        grade=int(input("{}".format(dict.keys())))
        print("\t第五题得分:{} 评语:{}".format(grade,dict[grade]))
        return [grade,dict[grade]]

    def giveGrade(self,ans_id:str,options_name:str,remark_name:str,exercise_number:int):
        function_map={
            1:self.exercise1,
            2:self.exercise2,
            3:self.exercise3,
            4: self.exercise4,
            5: self.exercise5,

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
                "ans_id":"a336",
                "options_name":"radio336",
                "remark_name":"txtRemark336"
            },
            2: {
                "ans_id": "a337",
                "options_name": "radio337",
                "remark_name": "txtRemark337"
            },
            3: {
                "ans_id": "a354",
                "options_name": "radio354",
                "remark_name": "txtRemark354"
            },
            4: {
                "ans_id": "a258",
                "options_name": "radio258",
                "remark_name": "txtRemark258"
            },
            5: {
                "ans_id": "a338",
                "options_name": "radio338",
                "remark_name": "txtRemark338"
            },
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
    ds1=DS3()
    ds1.assistant.login("http://1024.se.scut.edu.cn/")
    ds1.assistant.gotoAssignment("课后练习(程序控制结构）")
    ds1.assistant.checkAssignment()
    ds1.passAll()