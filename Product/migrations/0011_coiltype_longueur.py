# Generated by Django 4.0 on 2022-01-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_merge_20220105_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='coiltype',
            name='longueur',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Longueur Micronnage'),
        ),
    ]