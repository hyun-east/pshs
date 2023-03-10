# Generated by Django 3.1.3 on 2023-02-02 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pshs', '0003_auto_20230202_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lib_room', models.IntegerField()),
                ('lib_num', models.IntegerField()),
                ('class_num', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('check_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Recurit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('email', models.TextField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('clsss_num', models.IntegerField()),
                ('email', models.TextField()),
                ('recurit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pshs.recurit')),
            ],
        ),
    ]
