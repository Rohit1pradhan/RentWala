# Generated by Django 4.1.7 on 2023-04-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_varify'),
    ]

    operations = [
        migrations.CreateModel(
            name='varify_mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('verify_otp', models.CharField(max_length=20)),
            ],
        ),
    ]
