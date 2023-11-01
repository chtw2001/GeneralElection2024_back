# Generated by Django 3.2.22 on 2023-11-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('total_student_num', models.IntegerField()),
                ('voted_student_num', models.IntegerField()),
                ('win', models.CharField(max_length=128, null=True)),
                ('category', models.CharField(max_length=128, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
