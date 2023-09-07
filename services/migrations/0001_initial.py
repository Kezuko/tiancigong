from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('补运', '补运'), ('补财库', '补财库'), ('拜孔子', '拜孔子'), ('安太岁', '安太岁'), ('接财神', '接财神'), ('拜天狗', '拜天狗'), ('拜無鬼', '拜無鬼'), ('拜天宫', '拜天宫')], max_length=255)),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')], default='In Progress', max_length=50)),
                ('order_number', models.CharField(max_length=12, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(to='users.member')),
            ],
        ),
    ]
