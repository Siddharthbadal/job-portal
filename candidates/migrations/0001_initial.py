# Generated by Django 3.0.7 on 2020-06-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.TextField()),
                ('city', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100)),
                ('expected_salary', models.IntegerField()),
                ('will_relocate', models.BooleanField(default=True)),
            ],
        ),
    ]
