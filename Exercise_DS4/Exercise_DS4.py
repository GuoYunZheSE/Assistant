# @Date    : 15:59 04/16/2020
# @Author  : ClassicalPi
# @FileName: Exercise_DS4.py
# @Software: PyCharm

# For Exercise:函数

import time
from Assistant import Assistant


class DS4:
    def __init__(self):
        self.number = 3
        self.assistant = Assistant()

    def exercise2(self, ans: str) -> [int, str]:
        def test(a: int):
            sum = 0
            while a:  # while a 相当于 while a!=0
                sum += (a % 10)
                a = a // 10
            return sum

        comment = ""
        dict = {
            100: "结果正确，完全符合题目要求",
            90: "函数中用了全局变量或者print函数",
            80: "轻微错误，整体思路正确",
            60: "计算数字和，如果不用函数，至多给60分",
            30: "计算数字和，如果不用函数，至多给60分",
            0: "语法思路均不正确"
        }
        scope = {}
        print(ans)
        for case in [1, 98]:
            try:
                print("测试用例为:{}".format(case))
                exec(ans, scope)
                print("正确结果为:{}".format(test(case)))
                judge: str = input("是否运行成功？T/F")
                if judge == "T":
                    comment += "测试数据{}测试成功;".format(case)
                else:
                    comment += "测试数据{}测试失败，原因：结果错误，应该是:{}".format(case, test(case))
                    grade = input("\t请输入评分:{}".format(list(dict.keys())))
                    comment += dict[int(grade)]
                    print("\t第二题得分:{} 评语:{}".format(grade, comment))
                    return [int(grade), comment]
            except Exception:
                comment += "测试数据{}测试失败，原因：语法错误".format(case)
                print("\t" + comment)
                grade = input("\t请输入评分:{}".format(list(dict.keys())))
                comment += dict[int(grade)]
                print("\t第二题得分:{} 评语:{}".format(grade, comment))
                return [int(grade), comment]
        grade = int(input("\t请输入评分:{}".format(list(dict.keys()))))
        comment += dict[int(grade)]
        print("\t第二题得分:{} 评语:{}".format(grade, comment))
        return [grade, comment]

    def exercise1(self, ans: str) -> [int, str]:
        grade = 0
        comment = ""
        ans = ans.split('\n')
        if len(ans) == 0:
            comment = "该题未完成！"
            return [0, comment]
        Reference_answer = ['5', '24', '6']
        if len(ans) == 1 and (ans == "5 24 6" or ans == "5246" or ans == "5 24 6 "):
            comment = "没有换行哦，要扣一部分分数"
            return [80, comment]
        if len(ans) > len(Reference_answer):
            grade = int(input("第二题手动评分"))
            comment = "输入的答案规模大于参考答案规模，视情况给分"
            return [grade, comment]
        for i in range(len(ans)):
            if ans[i] == Reference_answer[i]:
                if i == 0:
                    grade += 30
                if i == 1:
                    grade += 30
                if i == 2:
                    grade += 40
                comment += "第{}行输出正确 ".format(i)
            else:
                comment += "第{}行出错，应该是:{}".format(i, Reference_answer[i])
        print("\t第二题得分:{} 评语:{}".format(grade, comment))
        return [grade, comment]

    def exercise3(self, ans: str) -> [int, str]:
        if ans == "" or ans == " ":
            return [0, "题目未完成"]

        def test(s):
            ct = 0
            for c in s:
                if c >= 'A' and c <= 'Z':
                    ct += 1
            return ct

        dict = {
            100: "结果正确，符合要求",
            50: "程序无法运行，有语法错误，最多给50分,根据错误的严重程度，如果只是少了冒号、括号不匹配，缩进不对的情况，稍作修改可以获得正确结果，则给50分",
            30: "有逻辑错误，比如不是返回大写字母个数，扣70",
            0: "程序无法运行，思路完全错误"
        }
        for testcase in ["SCut"]:
            try:
                print("TestCase:{}".format(testcase))
                scope = {}
                print(ans)
                print("正确结果为:{}".format(test(testcase)))
                exec(ans, scope)
            except:
                print("语法错误")
        grade = int(input("{}".format(list(dict.keys()))))
        print("\t第三题得分:{} 评语:{}".format(grade, dict[grade]))
        return [grade, dict[grade]]

    def giveGrade(self, ans_id: str, options_name: str, remark_name: str, exercise_number: int):
        function_map = {
            1: self.exercise1,
            2: self.exercise2,
            3: self.exercise3,
        }
        ans = self.assistant.chrome.find_element_by_id(ans_id).text
        grade, comment = function_map[exercise_number](ans)
        options = self.assistant.chrome.find_elements_by_name(options_name)
        options[int(grade / 10)].click()
        remark = self.assistant.chrome.find_element_by_name(remark_name)
        remark.send_keys(comment)

    def passAll(self):
        info = self.assistant.chrome.find_element_by_id("cmdNextStudent")
        student_left = info.get_attribute('value').split('(')
        student_left = int(student_left[1].strip(')'))
        keys=[351,416,417]
        dict = {
            1: {
                "ans_id": "a{}".format(keys[0]),
                "options_name": "radio{}".format(keys[0]),
                "remark_name": "txtRemark{}".format(keys[0])
            },
            2: {
                "ans_id": "a{}".format(keys[1]),
                "options_name": "radio{}".format(keys[1]),
                "remark_name": "txtRemark{}".format(keys[1])
            },
            3: {
                "ans_id": "a{}".format(keys[2]),
                "options_name": "radio{}".format(keys[2]),
                "remark_name": "txtRemark{}".format(keys[2])
            }
        }
        while student_left >= 0:
            print("{}: Student-{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), student_left))
            student_left -= 1
            for i in dict.keys():
                self.giveGrade(
                    ans_id=dict[i]["ans_id"],
                    options_name=dict[i]["options_name"],
                    remark_name=dict[i]["remark_name"],
                    exercise_number=int(i)
                )
            print(
                "{}:Student-{}评分完成，前往下一评分页面".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                                    student_left + 1))
            self.assistant.chrome.find_element_by_id("cmdNextStudent").click()
            self.assistant.chrome.implicitly_wait(2)


if __name__ == '__main__':
    ds1 = DS4()
    ds1.assistant.login("http://1024.se.scut.edu.cn/")
    ds1.assistant.gotoAssignment("课后练习（函数1）")
    ds1.assistant.checkAssignment()
    ds1.passAll()
