# Generated by Django 4.1.7 on 2023-04-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('activation', models.CharField(max_length=10)),
                ('current_city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='addhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('house_type', models.CharField(max_length=100)),
                ('rent', models.CharField(max_length=20)),
                ('facing', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('conditions', models.CharField(max_length=200)),
                ('facillities', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='reset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('OTP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='varify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField()),
                ('verification_otp', models.CharField(max_length=20)),
            ],
        ),
    ]