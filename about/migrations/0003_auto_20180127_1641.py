# Generated by Django 2.0.1 on 2018-01-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20180127_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='contact',
            field=models.EmailField(help_text='Enter your email', max_length=250),
        ),
        migrations.AlterField(
            model_name='about',
            name='occupation_why',
            field=models.CharField(max_length=30, verbose_name='Why do you like you work?'),
        ),
    ]
