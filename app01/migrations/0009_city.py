# Generated by Django 4.2.5 on 2023-09-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_rename_files_boss_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('count', models.IntegerField(verbose_name='人口')),
                ('img', models.FileField(max_length=128, upload_to='city/', verbose_name='Logo')),
            ],
        ),
    ]
