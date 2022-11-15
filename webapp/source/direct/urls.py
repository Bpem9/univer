from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)  # 127.0.0.1/api/v1/courses
router.register(r'groups', GroupsViewSet)   # 127.0.0.1/api/v1/groups
router.register(r'supervisors', SupervisorViewSet)  # 127.0.0.1/api/v1/supervisors
router.register(r'students', StudentsViewSet)   # 127.0.0.1/api/v1/students
router.register(r'disciplines', DisciplineViewSet)  # 127.0.0.1/api/v1/disciplines

urlpatterns = [
    path('', include(router.urls)),
    path('report/', Report.as_view(), name='report')


]