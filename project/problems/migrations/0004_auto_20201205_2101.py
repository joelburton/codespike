# Generated by Django 3.1.4 on 2020-12-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_studentproblem_studentproblemsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproblemsubmission',
            name='results',
            field=models.JSONField(blank=True, help_text='JSON of results of test cases.'),
        ),
    ]
