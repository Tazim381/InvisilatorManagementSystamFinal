# Generated by Django 4.0.5 on 2023-03-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examcommitte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('numberOfStudent', models.IntegerField()),
            ],
        ),
    ]
