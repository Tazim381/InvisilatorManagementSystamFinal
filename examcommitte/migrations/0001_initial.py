# Generated by Django 4.0.5 on 2023-03-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherID', models.CharField(default='1', max_length=25, null=True)),
                ('userName', models.CharField(max_length=25)),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('isCommittee', models.CharField(max_length=25)),
                ('isHeadOfCommittee', models.CharField(max_length=25)),
            ],
        ),
    ]
