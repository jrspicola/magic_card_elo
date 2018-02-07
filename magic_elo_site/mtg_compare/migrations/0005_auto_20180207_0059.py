# Generated by Django 2.0.1 on 2018-02-07 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_compare', '0004_auto_20180207_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardranking',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardranking',
            name='card',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mtg_compare.Card'),
        ),
    ]
