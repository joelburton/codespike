# Generated by Django 3.1.4 on 2020-12-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together={('id', 'title')},
        ),
    ]
