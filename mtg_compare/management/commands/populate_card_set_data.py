from django.core.management.base import BaseCommand
from mtg_compare.models import Card, CardRanking, CardType, CardColor, CardSet

class Command(BaseCommand):
    help = 'Load the dynamic data for Cards, Sets and Rankings - These are constant and should not change.'

    def add_arguments(self, parser):
        parser.add_argument(
                '--file',
                type=str,
                action='store',
                dest='fileName',
                help='Name of the file containing the card info to upload'
            )

    def _create_card_sets(self):
        pass

    def handle(self, *args, **options):
        print(options)