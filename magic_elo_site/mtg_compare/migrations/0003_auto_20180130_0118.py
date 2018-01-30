# Generated by Django 2.0.1 on 2018-01-30 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_compare', '0002_auto_20180130_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elo', models.IntegerField(default=1400, help_text='Enter the starting Elo for this card')),
            ],
        ),
        migrations.RemoveField(
            model_name='card',
            name='elo',
        ),
        migrations.AddField(
            model_name='cardranking',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg_compare.Card'),
        ),
    ]
