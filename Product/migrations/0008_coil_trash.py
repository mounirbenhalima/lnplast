# Generated by Django 4.0 on 2022-01-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_alter_coil_capacity_alter_coil_the_print_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coil',
            name='trash',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=6, null=True),
        ),
    ]
