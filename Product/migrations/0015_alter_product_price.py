# Generated by Django 4.0 on 2022-02-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0014_package_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Prix'),
        ),
    ]