# Generated by Django 2.1.5 on 2021-02-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
