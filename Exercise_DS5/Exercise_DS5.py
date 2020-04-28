# @Date    : 10:43 04/25/2020
# @Author  : ClassicalPi
# @FileName: Exercise_DS5.py
# @Software: PyCharm

# For Exercise:课后练习 (函数2)
import time
import random
from Assistant import Assistant

class DS5():
    def __init__(self):
        self.number=5
        self.assistant=Assistant()
    def exercise1(self, ans: str) -> [int, str]:
        def test(n):
            def fib(n):
                if n == 1 or n == 2:
                    return 1
                else:
                    return fib(n - 1) + fib(n - 2)

            return fib(n)

        grade = 100
        comment = ""
        ans = ans.split('\n')

        if len(ans) < 3:
            print("答案不完整，请检查")
            return [0, "答案不完整，请检查"]

        for j in range(len(ans)):
            for i in range(0, len(ans[j])):
                if ord(ans[j][i]) >= 97 and ord(ans[j][i]) <= 122:
                    ans[j] = ans[j][i::]
                    break

        for j in [1,2,12]:
            scope = {}
            i=random.randint(1,25)
            expr = """def fib(n):\n\tif {}:\n\t\treturn 1 \n\telse:\n\t\treturn {}+{}\nn = {}\ns=fib(n)\nprint(s)""".format(
                ans[0], ans[1], ans[2],i)
            try:
                exec(expr, scope)
                if scope['s'] != test(scope['n']):
                    grade = 0
                    comment += "输入{}运行出错，正确应该是{}而非{} ".format(scope['n'], test(scope['n']), scope['s'])
                else:
                    comment += "输入{}运行正确 ".format(scope['n'])
            except Exception:
                grade = 0
                comment += " 部分语法错误，无法运行"
                break
        print("\t第二题得分:{} 评语:{}".format(grade, comment))
        return [grade, comment]

    def exercise2(self, ans: str) -> [int, str]:
        grade = 0
        comment = ""
        ans = ans.split('\n')
        if len(ans) == 0:
            comment = "该题未完成！"
            return [0, comment]
        Reference_answer = ["55", "5050"]

        if ans=="555050" or ans == "55 5050":
            comment="没有换行，部分正确"
            return [50, comment]

        for i in range(len(ans)):
            if ans[i] == Reference_answer[i]:
                if i == 0:
                    grade += 50
                if i == 1:
                    grade += 50
                comment += "第{}行输出正确 ".format(i)
            else:
                comment += "第{}行出错，应该是:{}".format(i, Reference_answer[i])
        print("\t第2题得分:{} 评语:{}".format(grade, comment))
        return [grade, comment]

    def exercise3(self,ans:str)->[int,str]:
        def jump(n):
            if n == 1 or n == 2:
                return n
            else:
                return jump(n - 1) + jump(n - 2)
        if ans=="" or ans==" ":
            return [0,"题目未完成"]
        dict={
            100:"结果正确，符合要求",
            50:"语法错误或者输出的不是完数的数量，但是整体思路正确；或者没用递归，完成了题目",
            20:"输出结果不正确，思路部分正确",
            0:"输出结果不正确，思路不正确"
        }
        try:
            scope={}
            exec (ans,scope)
            print(jump(int(input("测试数据，输入级数"))))
        except:
            print("语法错误")
        grade=int(input("{}".format(dict.keys())))
        print("\t第3题得分:{} 评语:{}".format(grade,dict[grade]))
        return [grade,dict[grade]]

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
        keys=[377,412,418]
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
    ds1=DS5()
    ds1.assistant.login("http://1024.se.scut.edu.cn/")
    ds1.assistant.gotoAssignment("课后练习（函数2）")
    ds1.assistant.checkAssignment()
    ds1.passAll()