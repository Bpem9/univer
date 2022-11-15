from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q, Count


class Administrator(models.Model):
    name = models.OneToOneField(User, null=True, on_delete=models.CASCADE,
                                verbose_name='Имя пользователя администратора')
    last_name = models.CharField(max_length=50, null=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    patronym = models.CharField(max_length=50, null=True, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronym}'


class Supervisor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Имя пользователя куратора')
    last_name = models.CharField(max_length=50, null=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    patronym = models.CharField(max_length=50, null=True, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronym}'


class Course(models.Model):
    name = models.CharField(max_length=250, null=True, verbose_name='Направление подготовки')
    disciplines = models.ManyToManyField('Discipline', verbose_name='Дисциплины')
    supervisor = models.ForeignKey('Supervisor', related_name='courses', default=1, on_delete=models.SET_DEFAULT,
                                   verbose_name='Куратор')

    class Meta:
        verbose_name = 'Направление подготовки'
        verbose_name_plural = 'Направления подготовки'

    def __str__(self):
        return self.name


class StudentGroup(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Название группы')
    course = models.ForeignKey('Course', null=True, on_delete=models.SET_NULL,
                               verbose_name='Выбранное направление подготовки')


    class Meta:
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'


    def __str__(self):
        return self.name


class Student(models.Model):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    last_name = models.CharField(max_length=50, null=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    patronym = models.CharField(max_length=50, null=True, verbose_name='Отчество')
    gender = models.CharField(max_length=1, default='m', choices=GENDERS, verbose_name='Пол')
    birth_date = models.DateField(null=True, verbose_name='дата рождения')
    group = models.ForeignKey('StudentGroup', null=True, on_delete=models.SET_NULL, related_name='students',
                              verbose_name='Группа, в которую зачислен')



    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronym}'


class Discipline(models.Model):
    name = models.CharField(max_length=150, unique=True, default='Новая дисциплина')

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name
