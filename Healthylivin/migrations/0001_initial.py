# Generated by Django 4.2 on 2023-04-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('idnum', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
    ]