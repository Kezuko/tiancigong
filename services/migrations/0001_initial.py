# Generated by Django 4.1.10 on 2023-09-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('补运', '补运'), ('补财库', '补财库'), ('拜孔子', '拜孔子'), ('安太岁', '安太岁'), ('接财神', '接财神'), ('拜天狗', '拜天狗'), ('拜無鬼', '拜無鬼'), ('拜天宫', '拜天宫')], max_length=255)),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')], default='In Progress', max_length=50)),
                ('order_number', models.CharField(max_length=12, unique=True)),
            ],
        ),
    ]
