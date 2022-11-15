from django.db.models import Count, Value
from direct.constants import MAX_STUDENTS_IN_A_GROUP
from direct.models import *
import numpy as np
import pandas as pd
from slugify import slugify


class ADMReport:
    COURSE_QS = Course.objects.all()
    STUDENTGROUP_QS = StudentGroup.objects.annotate(
        men=Count('students'),
        women=Count('students'),
        vacant=MAX_STUDENTS_IN_A_GROUP - Count('students')
    )

    def __init__(self, file_manager=None):
        if not file_manager:
            self.file_manager = FileManager()
        else:
            self.file_manager = file_manager

    @classmethod
    def course_report(cls):
        courses = {}
        name = 'Курсы'
        for course in cls.COURSE_QS:
            courses[course.id] = {
                'Название курса': course.name,
                'Дисциплины': [value['name'] for value in course.disciplines.values()],
                'Куратор': str(course.supervisor)
            }
        return (courses, name)

    @classmethod
    def studentgroup_report(cls):
        studentgroups = {}
        name = 'Группы студентов'
        for group in cls.STUDENTGROUP_QS:
            studentgroups[group.id] = {
                'Название группы': group.name,
                'Студенты': sorted([str(student) for student in group.students.all()]),
                'Мужчин': group.men,
                'Женщин': group.women,
                'Свободных мест': group.vacant,
            }
        return (studentgroups, name)

    def report_generating(self, report_tuple):
        print(self.file_manager.pd_to_excel(report_tuple))

class FileManager:
    @staticmethod
    def pd_to_excel(report_tuple):
        report, name = report_tuple
        pd_report = pd.DataFrame(report, index=list(report.values())[0].keys(), columns=report.keys())
        pd_report.to_excel(f'../source/reports/{slugify(name)}_report.xlsx', sheet_name='Sheet1')
        return f'Report "{name}" generated'






