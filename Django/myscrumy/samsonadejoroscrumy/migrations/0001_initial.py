# Generated by Django 2.1.5 on 2019-03-24 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumProjectRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Scrum Users',
                'ordering': ['nickname'],
            },
        ),
       migrations.AddField(
            model_name='scrumprojectrole',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsonadejoroscrumy.ScrumUser'),
        ),
    ]
