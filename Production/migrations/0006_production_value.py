# Generated by Django 4.0 on 2022-03-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0005_production_user2_production_user3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
