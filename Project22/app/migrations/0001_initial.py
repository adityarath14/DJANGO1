# Generated by Django 5.0.1 on 2024-09-20 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BONUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENAME', models.CharField(max_length=10)),
                ('JOB', models.CharField(max_length=9)),
                ('SAL', models.IntegerField(max_length=4)),
                ('COMM', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DEPTNO', models.IntegerField(max_length=2, primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=14)),
                ('LOC', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='SALGRADE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GRADE', models.IntegerField(max_length=2)),
                ('LOSAL', models.IntegerField(max_length=2)),
                ('HISAL', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('EMPNO', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=10)),
                ('JOB', models.CharField(max_length=9)),
                ('MGR', models.IntegerField(max_length=4)),
                ('HIREDATE', models.DateField()),
                ('SAL', models.FloatField(max_length=7)),
                ('COMM', models.FloatField(max_length=7)),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
