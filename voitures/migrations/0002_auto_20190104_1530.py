# Generated by Django 2.1.4 on 2019-01-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voitures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='montant',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='marques',
            name='coutparjour',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='penalisation',
            name='cout',
            field=models.IntegerField(max_length=3),
        ),
    ]
