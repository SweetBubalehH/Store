# Generated by Django 3.0.6 on 2020-05-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='description',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
