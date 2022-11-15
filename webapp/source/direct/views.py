
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsSupervisorOrSUPEROrReadOnly, IsAdministratorOrSUPEROrReadOnly, IsAdministratorOrSUPEROrClosed
from .serializers import *
from .services import *
from . import tasks



class CourseViewSet(viewsets.ModelViewSet):
    """Отображение, создание, просмотр, редактирование и удаление курсов"""
    queryset = Course.objects.all()
    permission_classes = (IsAdministratorOrSUPEROrReadOnly,)



    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create' or self.action == 'update':
            return CourseSerializer
        else:
            return CourseListSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Отображение, создание, просмотр, редактирование и удаление групп студентов"""
    permission_classes = (IsSupervisorOrSUPEROrReadOnly,)
    queryset = StudentGroup.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create' or self.action == 'update':
            return StudentGroupsSerializer
        else:
            return StudentGroupsListSerializer


class SupervisorViewSet(viewsets.ModelViewSet):
    """Отображение, создание, просмотр, редактирование и удаление кураторов"""
    queryset = Supervisor.objects.all()
    serializer_class = CreateSupervisorSerializer
    permission_classes = (IsAdministratorOrSUPEROrReadOnly,)

class DisciplineViewSet(viewsets.ModelViewSet):
    """Отображение, создание, просмотр, редактирование и удаление дисциплин"""
    queryset = Discipline.objects.all()
    serializer_class = CreateDisciplineSerializer
    permission_classes = (IsSupervisorOrSUPEROrReadOnly,)

class StudentsViewSet(viewsets.ModelViewSet):
    """Отображение, создание, просмотр, редактирование и удаление студентов"""
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer
    permission_classes = (IsSupervisorOrSUPEROrReadOnly,)


class Report(APIView):
    permission_classes = (IsAdministratorOrSUPEROrClosed,)
    def get(self, request):
        results = tasks.generate_a_report.delay()
        return Response({'Done'})

