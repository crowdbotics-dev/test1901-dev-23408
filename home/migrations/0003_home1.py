# Generated by Django 2.2.26 on 2022-01-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BigIntegerField()),
            ],
        ),
    ]
