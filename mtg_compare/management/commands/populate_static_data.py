from django.core.management.base import BaseCommand
from mtg_compare.models import Card, CardRanking, CardType, CardColor, CardSet, CardRanking, CardComparison, CardComparisonResult

class Command(BaseCommand):
    args = ''
    help = 'Load the preliminary data for colors and card types - These are constant and should not change.'



    def _create_card_colors(self):
        CardColor(cardColor='White', colorAbrv='W').save()
        CardColor(cardColor='Blue', colorAbrv='U').save()
        CardColor(cardColor='Black', colorAbrv='B').save()
        CardColor(cardColor='Red', colorAbrv='R').save()
        CardColor(cardColor='Green', colorAbrv='G').save()
        CardColor(cardColor='Colorless', colorAbrv='C').save()

    def _create_card_types(self):
        CardType(cardType='Land').save()
        CardType(cardType='Creature').save()
        CardType(cardType='Artifact').save()
        CardType(cardType='Enchantment').save()
        CardType(cardType='Planeswalker').save()
        CardType(cardType='Instant').save()
        CardType(cardType='Sorcery').save()
        CardType(cardType='Tribal').save()
        CardType(cardType='Phenomenon').save()
        CardType(cardType='Plane').save()
        CardType(cardType='Scheme').save()
        CardType(cardType='Vanguard').save()
        CardType(cardType='Conspiracy').save()

    def handle(self, *args, **options):
        self._create_card_colors()
        self._create_card_types()