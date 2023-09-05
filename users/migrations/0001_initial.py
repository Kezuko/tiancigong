# Generated by Django 4.1.10 on 2023-09-05 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('member_id', models.CharField(default=users.utilities.generate_membership, editable=False, max_length=18, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('zip_code', models.CharField(max_length=6)),
                ('street_name', models.CharField(max_length=500)),
                ('block_number', models.CharField(max_length=10)),
                ('unit_number', models.CharField(default='#', max_length=40)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('eng_date_of_birth', models.DateField()),
                ('chi_date_of_birth', models.DateField()),
                ('zodiac', models.CharField(max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
