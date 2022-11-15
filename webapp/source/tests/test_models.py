from django.urls import reverse
from rest_framework import status
from rest_framework.serializers import ValidationError
from django.test import TestCase
from rest_framework.test import APITestCase

from direct.models import *

class StudentGroupsTestCase(APITestCase):
    def setUp(self) -> None:
        self.student_lst = [Student.objects.create(first_name=f'Student {i}') for i in range(21)]

    def test_student_assignment_while_group_creating(self):
        st = StudentGroup.objects.create(name='test_group1')
        st.students.set([self.student_lst[0], ])
        self.assertEqual(st.students.first(), self.student_lst[0], 'Студент не назначен')
        self.assertEqual(st.students.first().group_id, st.id, 'Группа студента при назначении не совпадает с назначаемой')


    def test_max_20_students_in_group(self):
        with self.assertRaises(ValidationError):
            st = StudentGroup.objects.create(name='test_group')
            st.students.set(self.student_lst)
            print('*' * 10, st.students.count(), '*' * 10)



