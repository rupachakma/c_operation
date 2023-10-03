# Generated by Django 4.2.5 on 2023-10-03 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('semester', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('batch', models.CharField(max_length=10)),
            ],
        ),
    ]