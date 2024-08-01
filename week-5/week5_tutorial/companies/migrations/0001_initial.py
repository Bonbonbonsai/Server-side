# Generated by Django 5.0.7 on 2024-08-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ticker', models.CharField(max_length=20, null=True)),
                ('num_employees', models.IntegerField()),
                ('num_tables', models.IntegerField()),
                ('num_chairs', models.IntegerField()),
            ],
        ),
    ]
