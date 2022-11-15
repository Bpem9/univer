from rest_framework import serializers
from .models import *
from direct.constants import MAX_STUDENTS_IN_A_GROUP






class CourseListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения кураторов в списке"""
    disciplines = serializers.SlugRelatedField(slug_field='name', queryset=Discipline.objects.all(), many=True)
    supervisor = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'disciplines', 'supervisor']




class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления кураторов в инпуте"""
    disciplines = serializers.SlugRelatedField(slug_field='name', queryset=Discipline.objects.all(), many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'disciplines', 'supervisor']




class StudentGroupsSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления студентов в группы в инпуте"""

    class Meta:
        model = StudentGroup
        fields = ['id', 'name', 'course', 'students']

    def validate(self, attrs):
        """Проверка на количество студентов в группе (при создании новой группы и при изменении существующей)"""
        if not self.instance:
            students = attrs['students']
            if len(students) > MAX_STUDENTS_IN_A_GROUP:
                raise serializers.ValidationError('Не допускается больше 20 студентов в группе')
        else:
            if len(self.initial_data.getlist('students')) > MAX_STUDENTS_IN_A_GROUP:
                raise serializers.ValidationError('Не допускается больше 20 студентов в группе')
        return attrs


class StudentGroupsListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения студентов в списке"""
    course = serializers.SlugRelatedField(slug_field='name', read_only=True)
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = StudentGroup
        fields = ['id', 'name', 'course', 'students']



class CreateDisciplineSerializer(serializers.ModelSerializer):
    """Добавление дицсиплин"""
    course_set = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Discipline
        fields = ['id', 'name', 'course_set']

class CreateStudentSerializer(serializers.ModelSerializer):
    """Добавление студентов"""
    class Meta:
        model = Student
        fields = '__all__'

    # def validate(self, attrs):
    #     print(attrs['group'])
    #     print(Student.objects.filter(group=attrs['group']))
    #     return attrs


class CreateSupervisorSerializer(serializers.ModelSerializer):
    """Добавление кураторов"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Supervisor
        fields = ['last_name', 'first_name', 'patronym', 'user']