# Generated by Django 2.2.1 on 2021-04-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('done', 'Done')], default='todo', max_length=10)),
            ],
        ),
    ]
