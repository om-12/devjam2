# Generated by Django 3.0.6 on 2020-05-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rentyourhouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('From', models.CharField(max_length=10)),
                ('To', models.CharField(max_length=10)),
                ('adults', models.CharField(max_length=1)),
                ('children', models.CharField(max_length=1)),
                ('phonenumber', models.CharField(max_length=10)),
                ('appointment', models.TimeField()),
            ],
        ),
    ]
