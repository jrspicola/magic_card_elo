# Generated by Django 2.0.1 on 2018-01-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_compare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='cardcolor',
            name='cardColor',
            field=models.CharField(help_text='Enter a color', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='cardset',
            name='cardSet',
            field=models.CharField(help_text='Enter the name of a set', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='cardtype',
            name='cardType',
            field=models.CharField(help_text='Enter a card type', max_length=50, unique=True),
        ),
    ]
