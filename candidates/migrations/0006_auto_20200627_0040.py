# Generated by Django 3.0.7 on 2020-06-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_auto_20200625_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatejobmap',
            old_name='stauts',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]