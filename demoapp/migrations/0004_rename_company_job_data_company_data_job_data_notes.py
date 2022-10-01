# Generated by Django 4.0.5 on 2022-07-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_remove_data_distance_remove_data_salary_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='Company_Job',
            new_name='Company',
        ),
        migrations.AddField(
            model_name='data',
            name='Job',
            field=models.CharField(default='Error', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='Notes',
            field=models.CharField(default=' ', max_length=10000),
        ),
    ]