# @Date    : 01:37 03/30/2020
# @Author  : ClassicalPi
# @FileName: Resubmit.py
# @Software: PyCharm
from Assistant import Assistant
class Resubmit:
    def __init__(self,exercise_name:str,dic:{str:{int:str}}):
        self.exercise_name=exercise_name
        self.assistant=Assistant
        self.dic=dic

    def submit(self):
        for student in self.dic.keys():
            try:
