# Generated by Django 3.2.8 on 2021-10-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contact_ssc_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ssc_memo',
            field=models.ImageField(null=True, upload_to='student/images'),
        ),
    ]