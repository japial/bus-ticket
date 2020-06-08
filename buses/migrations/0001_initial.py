# Generated by Django 3.0.7 on 2020-06-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('head_office', models.TextField()),
                ('staff_count', models.IntegerField(default=0)),
            ],
        ),
    ]