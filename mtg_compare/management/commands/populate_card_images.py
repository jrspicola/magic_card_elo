from django.core.management.base import BaseCommand
from mtg_compare.models import Card, CardRanking, CardType, CardColor, CardSet, CardRanking, CardComparison, CardComparisonResult
from mtgsdk import Card as Sdk_card_class

class Command(BaseCommand):
    args = ''
    help = 'Load the images for individual cards.'



    def _load_card_images(self):
        print('STARTING IMAGE REQUEST')
        for card in Card.objects.all():
            print(card.name)
            card.get_remote_image()
            print(card.image)

    def _set_card_urls(self):
        print('STARTING SET CARDS')
        for card in Card.objects.all():
            print(card.name)
            sdk_card_list = Sdk_card_class.where(name=card.name).all()
            if len(sdk_card_list) != 0:
                sdk_card = sdk_card_list[0]
                card.image_url = sdk_card.image_url
                card.save()
            else:
                print('none')

    def handle(self, *args, **options):
        #self._set_card_urls()
        self._load_card_images()