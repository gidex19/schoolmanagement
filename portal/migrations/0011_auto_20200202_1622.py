# Generated by Django 2.2.2 on 2020-02-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_customuser_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='passport',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='passports'),
        ),
    ]
