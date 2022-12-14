# Generated by Django 3.2.16 on 2022-11-06 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Направление подготовки')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
                'verbose_name_plural': 'Направления подготовки',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Новая дисциплина', max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('patronym', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1, verbose_name='Пол')),
                ('birth_date', models.DateField(null=True, verbose_name='дата рождения')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('patronym', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя куратора')),
            ],
            options={
                'verbose_name': 'Куратор',
                'verbose_name_plural': 'Кураторы',
            },
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название группы')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='direct.course', verbose_name='Выбранное направление подготовки')),
            ],
            options={
                'verbose_name': 'Группа студентов',
                'verbose_name_plural': 'Группы студентов',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='disciplines',
            field=models.ManyToManyField(to='direct.Discipline', verbose_name='Дисциплины'),
        ),
        migrations.AddField(
            model_name='course',
            name='supervisor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='courses', to='direct.supervisor', verbose_name='Куратор'),
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('patronym', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя администратора')),
            ],
            options={
                'verbose_name': 'Администратор',
                'verbose_name_plural': 'Администраторы',
            },
        ),
    ]
