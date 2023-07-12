# Generated by Django 3.2.8 on 2021-10-31 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='application',
            name='gender',
        ),
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.CharField(choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Information Technology', 'Information Technology'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Biotechnology', 'Biotechnology')], default='Choose Your Course', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='None', max_length=128),
        ),
        migrations.CreateModel(
            name='Student_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Information Technology', 'Information Technology'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Biotechnology', 'Biotechnology')], max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=128)),
                ('DOB', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('student_profile', models.ImageField(upload_to='images')),
                ('ssc_score', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('ssc_memo', models.ImageField(null=True, upload_to='images')),
                ('ssc_tc', models.ImageField(null=True, upload_to='images')),
                ('inter_score', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('inter_memo', models.ImageField(null=True, upload_to='images')),
                ('inter_tc', models.ImageField(null=True, upload_to='images')),
                ('eamcet_score', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('eamcet_memo', models.ImageField(null=True, upload_to='images')),
                ('jee_score', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('jee_memo', models.ImageField(null=True, upload_to='images')),
                ('Application_Status', models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('message', models.TextField(blank=True, default='', max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]