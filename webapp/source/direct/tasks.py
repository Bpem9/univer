from celery import Celery
from celery import shared_task
from university_direction.celery import app
from .services import *


@shared_task
def generate_a_report():
    ro = ADMReport()
    courses_report = ro.course_report()
    groups_report = ro.studentgroup_report()
    result1 = ro.report_generating(groups_report)
    result2 = ro.report_generating(courses_report)
    return (result1, result2)