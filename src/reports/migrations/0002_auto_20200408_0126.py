# Generated by Django 3.0.5 on 2020-04-08 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='carton_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateTimeField(null=True),
        ),
    ]
