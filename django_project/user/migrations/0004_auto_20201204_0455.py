# Generated by Django 3.1.3 on 2020-12-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201204_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dj_user',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=8, null=True, verbose_name='등급'),
        ),
    ]
