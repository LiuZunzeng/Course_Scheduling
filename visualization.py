# -*- coding:utf-8 -*-
"""
@Time:2023/11/29
@Auth:Liu Zunzeng
@File:visualization.py
"""
import matplotlib
matplotlib.rc("font",family='STSong')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class CourseSchedule:
    def __init__(self, num_days, num_time_slots, num):
        self.num_days = num_days  # 总天数
        self.num_time_slots = num_time_slots  # 总时段
        self.schedule = np.empty((num_days, num_time_slots), dtype=object)  # 课表
        self.num = num

    def add_course(self, teacher, course, day, time_slot, duration, classroom):
        self.schedule[day, time_slot] = {
            'course': course,
            'duration': duration,
            'teacher': teacher,
            'classroom': classroom
        }

    def plot_schedule(self):
        matplotlib.rc("font", family='STSong')
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xticks(np.arange(-0.5, self.num_days))
        ax.set_yticks(np.arange(-0.5, self.num_time_slots))
        ax.set_xticklabels(range(1, self.num_days + 1))
        ax.set_yticklabels(range(1, self.num_time_slots + 1))
        ax.grid(color='gray', linestyle='-', linewidth=1.5)

        # 设置纵坐标范围
        #ax.set_ylim(-0.5, self.num_time_slots - 0.5)
        #ax.set_xlim(-0.5, self.num_days - 0.5 * (3 / 2))
        ax.set_aspect(0.6)  # 设置纵横比为1，使网格单元格为正方形

        for i in range(self.num_days):
            for j in range(self.num_time_slots):
                if self.schedule[i, j] is not None:
                    course_info = self.schedule[i, j]
                    course = course_info['course']
                    duration = course_info['duration']
                    teacher = course_info['teacher']
                    classroom = course_info['classroom']
                    ax.add_patch(Rectangle((i - 0.5, j - 0.5), 1, duration, facecolor='lightblue', edgecolor='black', linewidth=2))
                    ax.text(i, j+(duration - 1)/2, f"{course}\n{teacher}\n{classroom}", ha='center', va='center' , fontsize=17, fontweight='bold')

        plt.xlabel('Days')
        plt.ylabel('Time Slots')
        plt.title('N0.%d Course Schedule'%self.num)
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    # 创建课表对象
    course_schedule = CourseSchedule(num_days=5, num_time_slots=12, num = 4)

    # 添加课程信息
    '''#管科的原始课表
    course_schedule.add_course("wc", "A", day=0, time_slot=4, duration=2, classroom="主楼333")
    course_schedule.add_course("alp", "B", day=0, time_slot=6, duration=2, classroom="学院520")
    course_schedule.add_course("zjy", "C", day=0, time_slot=8, duration=2, classroom="学院520")
    course_schedule.add_course("wj", "D", day=1, time_slot=2, duration=2, classroom="学院621")
    course_schedule.add_course("zsc", "E", day=2, time_slot=4, duration=2, classroom="学院521")
    course_schedule.add_course("njb", "F", day=2, time_slot=8, duration=3, classroom="学院A502")
    course_schedule.add_course("yjl", "G", day=3, time_slot=0, duration=3, classroom="学院520")
    course_schedule.add_course("wds", "H", day=3, time_slot=8, duration=3, classroom="学院620")
    course_schedule.add_course("lrh", "I", day=4, time_slot=2, duration=2, classroom="学院622")
    course_schedule.add_course("lyj", "J", day=4, time_slot=8, duration=2, classroom="学院A501-3")
    '''
    '''#会计的原始课表
    course_schedule.add_course("wc", "A", day=0, time_slot=4, duration=2, classroom="主楼333")
    course_schedule.add_course("gzh", "H", day=1, time_slot=0, duration=3, classroom="学院521")
    course_schedule.add_course("zjx", "K", day=1, time_slot=4, duration=4, classroom="学院620")
    course_schedule.add_course("jyf", "L", day=2, time_slot=4, duration=3, classroom="学院620")
    course_schedule.add_course("njb", "F", day=2, time_slot=8, duration=3, classroom="学院A502")
    course_schedule.add_course("ls", "M", day=3, time_slot=0, duration=3, classroom="学院521")
    course_schedule.add_course("zl", "N", day=3, time_slot=8, duration=3, classroom="学院621")
    course_schedule.add_course("wj", "O", day=4, time_slot=3, duration=2, classroom="学院520")
    '''
    '''#企业管理的原始课表
    course_schedule.add_course("md", "P", day=0, time_slot=0, duration=2, classroom="学院521")
    course_schedule.add_course("wc", "A", day=0, time_slot=4, duration=2, classroom="主楼333")
    course_schedule.add_course("zgp", "Q", day=1, time_slot=4, duration=3, classroom="学院521")
    course_schedule.add_course("yb", "R", day=2, time_slot=0, duration=3, classroom="学院620")
    course_schedule.add_course("njb", "F", day=2, time_slot=8, duration=3, classroom="学院A502")
    course_schedule.add_course("xh", "S", day=3, time_slot=0, duration=3, classroom="学院620")
    course_schedule.add_course("wds", "H", day=3, time_slot=8, duration=3, classroom="学院620")
    course_schedule.add_course("zxn", "T", day=4, time_slot=4, duration=2, classroom="学院621")
    '''
    #公司治理的原始课表
    course_schedule.add_course("wc", "A", day=0, time_slot=4, duration=2, classroom="主楼333")
    course_schedule.add_course("lwa", "U", day=0, time_slot=8, duration=4, classroom="学院521")
    course_schedule.add_course("wds", "V", day=1, time_slot=0, duration=2, classroom="学院619")
    course_schedule.add_course("njb", "W", day=1, time_slot=4, duration=3, classroom="学院622")
    course_schedule.add_course("hc", "X", day=2, time_slot=0, duration=3, classroom="学院422")
    course_schedule.add_course("njb", "F", day=2, time_slot=8, duration=3, classroom="学院A502")
    course_schedule.add_course("wll", "Y", day=4, time_slot=0, duration=3, classroom="学院621")

    # 可视化课表
    course_schedule.plot_schedule()