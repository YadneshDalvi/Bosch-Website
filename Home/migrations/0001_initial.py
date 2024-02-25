# Generated by Django 5.0.2 on 2024-02-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('branch', models.CharField(max_length=122)),
                ('reason', models.CharField(max_length=500)),
                ('file', models.BinaryField()),
            ],
        ),
    ]
