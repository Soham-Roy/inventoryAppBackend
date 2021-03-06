# Generated by Django 3.2.5 on 2021-07-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventoryName', models.CharField(max_length=80)),
                ('ownerClub', models.CharField(max_length=80)),
                ('available', models.IntegerField()),
                ('quantityTotal', models.IntegerField()),
                ('lastUpdated', models.IntegerField()),
            ],
        ),
    ]
