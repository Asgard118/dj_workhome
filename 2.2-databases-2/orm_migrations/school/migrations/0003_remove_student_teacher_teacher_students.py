# Generated by Django 4.2.7 on 2023-11-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='teachers', to='school.student', verbose_name='Ученики'),
        ),
    ]
