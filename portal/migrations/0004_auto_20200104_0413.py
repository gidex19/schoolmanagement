# Generated by Django 2.2.2 on 2020-01-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20200104_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='admission_no',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state_of_origin',
            field=models.CharField(blank=True, choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Anambra', 'Anambra'), ('Akwa Ibom', 'Akwa Ibom'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Enugu', 'Enugu'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('FCT - Abuja', 'FCT - Abuja'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=20),
        ),
    ]
