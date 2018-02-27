# Generated by Django 2.0.1 on 2018-02-27 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('cmc', models.IntegerField(default=0, help_text='Enter the converted mana cost of this card')),
            ],
        ),
        migrations.CreateModel(
            name='CardColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardColor', models.CharField(help_text='Enter a color', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardComparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leftCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_card', to='mtg_compare.Card')),
                ('rightCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_card', to='mtg_compare.Card')),
            ],
        ),
        migrations.CreateModel(
            name='CardComparisonResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comparison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg_compare.CardComparison')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losing_card', to='mtg_compare.Card')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winning_card', to='mtg_compare.Card')),
            ],
        ),
        migrations.CreateModel(
            name='CardRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elo', models.IntegerField(default=1400, help_text='Enter the starting Elo for this card')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mtg_compare.Card')),
            ],
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardSet', models.CharField(help_text='Enter the name of a set', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardType', models.CharField(help_text='Enter a card type', max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='cardColor',
            field=models.ManyToManyField(help_text='Select a color for this card', to='mtg_compare.CardColor'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardSet',
            field=models.ManyToManyField(help_text='Select a set this card is from', to='mtg_compare.CardSet'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardType',
            field=models.ManyToManyField(help_text='Select a type for this card', to='mtg_compare.CardType'),
        ),
    ]
