from django.core.management.base import BaseCommand
from mtg_compare.models import CardSet

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_card_sets(self):
        c = CardSet(cardSet='Return To Ravnica', code='RTR')
        c.save()

    def handle(self, *args, **options):
        self._create_card_sets()