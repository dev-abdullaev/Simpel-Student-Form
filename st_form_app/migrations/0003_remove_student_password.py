# Generated by Django 3.1.4 on 2021-01-18 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('st_form_app', '0002_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
