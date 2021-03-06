# Generated by Django 3.2.8 on 2021-11-01 16:05

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.baseuser')),
                ('enduser_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('address', models.TextField(default='')),
                ('phone', models.CharField(default=None, max_length=100)),
                ('panchayath_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enduser', to='users.panchayath')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
