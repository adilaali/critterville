# Generated by Django 4.1.7 on 2023-03-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('Phone_Number', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]