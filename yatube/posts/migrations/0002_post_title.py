# Generated by Django 4.2.5 on 2023-09-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(
                default=1, max_length=200, verbose_name='название'
            ),
            preserve_default=False,
        ),
    ]