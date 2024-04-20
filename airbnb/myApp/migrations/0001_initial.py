# Generated by Django 5.0.4 on 2024-04-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=20)),
                ('req_occupancy', models.CharField(choices=[('1', 'single-sharing'), ('2', 'double-sharing'), ('3', 'triple-sharing'), ('4', 'quad-sharing')], max_length=10)),
                ('gender', models.CharField(choices=[('1', 'male'), ('2', 'Female'), ('3', 'Other')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=20)),
                ('req_occupancy', models.CharField(choices=[('1', 'single-sharing'), ('2', 'double-sharing'), ('3', 'triple-sharing'), ('4', 'quad-sharing')], max_length=10)),
                ('gender', models.CharField(choices=[('1', 'male'), ('2', 'Female'), ('3', 'Other')], max_length=8)),
            ],
        ),
    ]
