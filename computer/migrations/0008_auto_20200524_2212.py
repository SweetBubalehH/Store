# Generated by Django 3.0.6 on 2020-05-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0007_auto_20200524_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='image',
            field=models.ImageField(blank=True, upload_to='computer/%Y/%m/%d'),
        ),
    ]
