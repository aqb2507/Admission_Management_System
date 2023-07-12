# Generated by Django 3.2.8 on 2021-10-31 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_contact_ssc_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='DOB',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='None', max_length=128),
        ),
    ]
