# Generated by Django 2.0.5 on 2018-06-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interns',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_id', models.IntegerField()),
                ('r_id', models.IntegerField()),
                ('s_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Internships',
            fields=[
                ('i_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_company', models.CharField(max_length=100)),
                ('i_logo', models.ImageField(upload_to='images/logo')),
                ('i_category', models.CharField(max_length=50)),
                ('i_skills', models.TextField()),
                ('i_number', models.IntegerField()),
                ('i_desc', models.TextField(max_length=400)),
                ('i_location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_email', models.EmailField(max_length=50)),
                ('r_password', models.TextField(max_length=20)),
                ('r_name', models.CharField(max_length=300)),
                ('r_dob', models.DateField()),
                ('r_phone', models.BigIntegerField()),
                ('r_company', models.TextField(max_length=500)),
                ('r_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_email', models.EmailField(max_length=50)),
                ('s_password', models.TextField(max_length=20)),
                ('s_name', models.TextField(max_length=300)),
                ('s_dob', models.DateField()),
                ('s_phone', models.BigIntegerField()),
                ('s_skills', models.TextField(max_length=500)),
                ('s_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
