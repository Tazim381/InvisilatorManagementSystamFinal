# Generated by Django 4.0.5 on 2023-03-26 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examcommitte', '0004_createdexamcommittee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('start', models.TimeField(null=True)),
                ('end', models.TimeField(null=True)),
                ('courseCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='examcommitte.course')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='examcommitte.semister')),
                ('teachers', models.ManyToManyField(to='examcommitte.teacher')),
            ],
        ),
    ]
