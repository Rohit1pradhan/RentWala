# Generated by Django 4.0.3 on 2023-06-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_addhouse_facilities_alter_addhouse_area_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addhouse',
            name='Facilities',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='area',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='conditions',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='house_facing',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='house_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='owner_contect_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='owner_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='picture1',
            field=models.FileField(upload_to='HousePictures'),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='picture2',
            field=models.FileField(upload_to='HousePictures'),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='picture3',
            field=models.FileField(upload_to='HousePictures'),
        ),
        migrations.AlterField(
            model_name='addhouse',
            name='rent',
            field=models.CharField(max_length=20),
        ),
    ]
