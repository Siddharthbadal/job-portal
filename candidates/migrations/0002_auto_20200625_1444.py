# Generated by Django 3.0.7 on 2020-06-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100),
        ),
    ]
