# Generated by Django 3.2.8 on 2021-11-18 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_enduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('ta', models.IntegerField()),
                ('da', models.IntegerField()),
                ('credited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='users.employee')),
                ('panchayath_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='users.panchayath')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('panchayath_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='users.panchayath')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('solved', models.BooleanField(default=False)),
                ('enduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.enduser')),
                ('panchayath_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='users.panchayath')),
            ],
        ),
    ]
