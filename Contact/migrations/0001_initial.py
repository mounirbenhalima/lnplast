# Generated by Django 3.1 on 2021-11-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom de Famille')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prénom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero de Téléphone')),
                ('contact_type', models.CharField(blank=True, choices=[('SUPPLIER', 'Fournisseur'), ('CLIENT', 'Client'), ('WORKSHOP', 'Atelier')], max_length=25, null=True, verbose_name='Type de Contact')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse')),
                ('region', models.CharField(blank=True, choices=[('ORAN', 'Oran')], max_length=255, null=True, verbose_name='Wilaya')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'Contact',
                'ordering': ['contact_type'],
            },
        ),
    ]