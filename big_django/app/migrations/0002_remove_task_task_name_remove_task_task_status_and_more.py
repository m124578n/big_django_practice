# Generated by Django 4.2.2 on 2024-01-02 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Task Name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Task Status',
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='test', max_length=65, unique=True, verbose_name='Task Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('u', 'Unstarted'), ('o', 'Ongoing'), ('f', 'Finished')], default='u', max_length=1, verbose_name='Task Status'),
            preserve_default=False,
        ),
    ]
