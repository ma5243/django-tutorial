# Generated by Django 3.1.6 on 2021-02-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_thoughts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thoughts',
            name='thoughtText',
            field=models.TextField(),
        ),
    ]
