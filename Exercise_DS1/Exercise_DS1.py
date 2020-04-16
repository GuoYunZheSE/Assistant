# @Date    : 14:48 03/19/2020
# @Author  : ClassicalPi
# @FileName: Assistant.py
# @Software: PyCharm

import sys
from io import StringIO
import contextlib
import pexpect
class DS1:

    def __init__(self):
        self.number=4

    def exercise1(self,ans:str)->[int,str]:
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
        print("\t第一题得分:{} 评语:{}".format(grade,comment))
        return [grade,comment]

    def exercise2(self,ans:str)->[int,str]:
        def test(n:str):
            s=0
            for i in n:
                s+=eval(i)**2
            return s
        grade = 100
        comment=""
        dict={
            100:"结果正确，并且使用input，有中文提示",
            90:"填空题只需填写空白部分即可",
            80:"部分结果正确",
            50:"语法错误，思路正确",
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

        for i in range(3):
            scope={}
            expr="""n = input("请输入一个正整数：")\ns=0\nfor i in {}:\n\ts=s+{}\nprint(s)""".format(ans[0],ans[1])
            try:
                exec (expr,scope)
                if scope['s']!=test(scope['n']):
                    grade=50
                    comment+="输入{}运行出错，正确应该是{}而非{} ".format(scope['n'],test(scope['n']),scope['s'])
                else:
                    comment += "输入{}运行正确 ".format(scope['n'])
            except Exception:
                grade=0
                comment+=" 部分语法错误，无法运行"
                break
        print("\t第二题得分:{} 评语:{}".format(grade,comment))
        return [grade,comment]

    def exercise3(self,ans:str)->[int,str]:
        # @contextlib.contextmanager
        # def stdoutIO(stdout=None):
        #     old = sys.stdout
        #     if stdout is None:
        #         stdout = StringIO()
        #     sys.stdout = stdout
        #     yield stdout
        #     sys.stdout = old
        if ans=="" or ans==" ":
            return [0,"题目未完成"]
        dict={
            100:"结果正确，并且使用input，有中文提示",
            80:"结果正确，但是没有符合题目规范",
            50:"输出结果不正确，思路正确或者无法处理小数",
            30:"输出结果不正确，思路部分正确",
            0:"输出结果不正确，思路不正确"
        }
        for i in range(3):
            try:
                scope={}
                exec (ans,scope)
            except:
                print("语法错误")
        grade=int(input("100|80|50|30|0"))
        print("\t第三题得分:{} 评语:{}".format(grade,dict[grade]))
        return [grade,dict[grade]]

    def exercise4(self,ans:str)->[int,str]:
        # @contextlib.contextmanager
        # def stdoutIO(stdout=None):
        #     old = sys.stdout
        #     if stdout is None:
        #         stdout = StringIO()
        #     sys.stdout = stdout
        #     yield stdout
        #     sys.stdout = old
        def test(a,b,c):
            import math
            p = (a + b + c) / 2.0
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            return s
        dict={
            100:"结果正确，符合要求",
            80:"无法处理小数",
            50:"结果错误，思路正确",
            30:"输出结果不正确，思路不正确",
            40:"海伦不正确，其他正确",
            0:"结果错误，思路严重错误"
        }
        comment=""
        for i in range(2):
            try:
                scope={}
                exec (ans,scope)
                if scope.__contains__('s'):
                    res=scope['s']
                elif scope.__contains__('S'):
                    res=scope['S']

                if "{:.2f}".format(res)=="{:.2f}".format(test(scope['a'],scope['b'],scope['c'])):
                    print("{},{},{} 测试通过".format(scope['a'],scope['b'],scope['c']))
                    comment+="{},{},{} 测试通过".format(scope['a'],scope['b'],scope['c'])
                else:
                    print("{},{},{} 测试未通过".format(scope['a'], scope['b'], scope['c']))
                    comment += "{},{},{} 测试未通过".format(scope['a'], scope['b'], scope['c'])
            except:
                print("语法错误")
        grade=int(input("100|50|30|40|0"))
        print("\t第四题得分:{} 评语:{}".format(grade,comment))
        return [grade,dict[grade]+comment]