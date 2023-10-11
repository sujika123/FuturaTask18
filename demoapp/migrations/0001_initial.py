# Generated by Django 4.2.3 on 2023-10-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=100)),
                ('DueDate', models.DateField(max_length=100)),
                ('Priority', models.IntegerField(default=0)),
            ],
        ),
    ]
