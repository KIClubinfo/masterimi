# Generated by Django 2.0.7 on 2018-07-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcours_imi', '0002_userparcours_conversation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userparcours',
            name='conversation',
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(max_length=20, verbose_name='Semestre'),
        ),
    ]
