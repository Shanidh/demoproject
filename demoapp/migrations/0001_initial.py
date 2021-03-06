# Generated by Django 4.0.4 on 2022-05-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('phone_num', models.BigIntegerField()),
                ('password', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
